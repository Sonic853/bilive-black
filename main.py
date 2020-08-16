import sys,Ui_black,Ui_login,configloader,json
from login import login
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.Qtcore import QString
from PyQt5.QtWidgets import QMessageBox
from bilibili import bilibili
# from PyQt5.QtWidgets import QApplication, QMainWindow

def button_pressed(self):
    print('Button pressed')

def button_pressed2(self):
    text = child_ui.lineEdit_u.text()
    print('Button pressed: '+text)

def showmsg(p,error,text):
    msg = QtWidgets.QMessageBox(p)
    # msg.setIcon(QtWidgets.QMessageBox.Critical)
    if error == "error":
        msg.setText("错误")
        msg.setWindowTitle("Error")
    elif error == "msg":
        msg.setText("信息")
        msg.setWindowTitle("Msg")
    msg.setInformativeText(text)
    msg.exec_()

def checklogin(ui,pw):
    if pw == "":
        ui.label_Login.setText("登录状态：未登录")
    else:
        ui.label_Login.setText("登录状态：已登录")

def trylogin(self):
    if str(child_ui.lineEdit_u.text()) == "" or str(child_ui.lineEdit_p.text()) == "" :
        showmsg(child,"error",'用户名和密码不能为空！')
    else:
        trytext = login().loginupc(username=str(child_ui.lineEdit_u.text()),password=str(child_ui.lineEdit_p.text()),c=str(child_ui.lineEdit_c.text()))
        if trytext != True:
            showmsg(child,"error",trytext)
        else:
            child.close()
            showmsg(MainWindow,"msg","登陆成功")
            ui.label_Login.setText("登录状态：已登录")

def openlogin(self):
    child.close()
    child_ui.lineEdit_u.setText(bilibili().dic_bilibili['account']['username'])
    child_ui.lineEdit_p.setText("")
    child_ui.lineEdit_c.setText("")
    reload_captcha()
    child.show()

def reload_captcha():
    img = login().get_captcha()
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(img)
    child_ui.label_3.setPixmap(pixmap)

def connect_room():
    if str(ui.RoomInput.text()) == "":
        showmsg(MainWindow,"error","房间号不能为空！")
    elif str(bilibili().dic_bilibili['account']['password']) == "":
        showmsg(MainWindow,"error","你尚未登录，请登录后再连接")
    else:
        roomid = ui.RoomInput.text()
        bilibili().dic_bilibili['account']['roomid'] = str(roomid)
        dic_saved_session = {
            'roomid': str(roomid)
        }
        configloader.write2bilibililogin(dic_saved_session)
        load_blacklist()

def load_blacklist():
    if str(ui.RoomInput.text()) == "":
        showmsg(MainWindow,"error","房间号不能为空！")
    else:
        url = "https://api.live.bilibili.com/liveact/ajaxGetBlockList?roomid="+bilibili().dic_bilibili['account']['roomid']+"&page=1"
        response = bilibili().get_data(url)
        if response != False:
            data = json.loads(response.text)
        # {"code":0,"msg":"","message":"","data":[{"id":5266858,"roomid":15667,"uid":2867557,"type":1,"adminid":1968333,"block_end_time":"2020-08-17 01:28:14","ctime":"2020-08-17 00:28:14","msg":"","msg_time":"","uname":"853","admin_uname":"Sonic853"}]}
            if data["code"] == 0:
                ui.tableWidget.setRowCount(0)
                if len(data["data"]) !=0:
                    for d in data["data"]:
                        rowPosition = ui.tableWidget.rowCount()
                        ui.tableWidget.insertRow(rowPosition)
                        ui.tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(str(d["id"])))
                        ui.tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(str(d["uname"])))
                        ui.tableWidget.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(str(d["uid"])))
                        ui.tableWidget.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(str(d["ctime"])))
                        ui.tableWidget.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(str(d["block_end_time"])))
                        ui.tableWidget.setItem(rowPosition , 5, QtWidgets.QTableWidgetItem(str(d["admin_uname"])))
            else:
                showmsg(MainWindow,"error","错误："+str(data["code"])+"，"+str(data["message"]))
                if data["code"] == 3:
                    ui.label_Login.setText("登录状态：登录已失效")

def block_user(self):
    if str(ui.RoomInput.text()) == "":
        showmsg(MainWindow,"error","房间号不能为空！")
    elif str(ui.BlackTimeInput.text()) == "":
        showmsg(MainWindow,"error","封禁时间不能为空！")
    elif str(ui.BlackUIDInput.text()) == "":
        showmsg(MainWindow,"error","用户名或UID不能为空！")
    else:
        user_items = search_user(str(ui.BlackUIDInput.text()))
        # print(user_items)
        if user_items != False:
            if len(user_items) == 1:
                send_block_user(str(user_items[0]["uid"]),str(ui.BlackTimeInput.text()))
            elif len(user_items) == 0:
                showmsg(MainWindow,"msg","找不到这个用户")
            elif len(user_items) == 2:
                reply = QMessageBox.question(MainWindow,'啊哦','找到两个用户<br><br>Yes 将选择（UID:'+str(user_items[0]["uid"])+' 用户名:'+str(user_items[0]["uname"])+'）的用户<br>No 将选择（UID:'+str(user_items[1]["uid"])+' 用户名:'+str(user_items[1]["uname"])+'）的用户<br><br>Cancel 或 关闭 将不做选择', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
                if reply == QMessageBox.Yes:
                    send_block_user(str(user_items[0]["uid"]),str(ui.BlackTimeInput.text()))
                elif reply == QMessageBox.No:
                    send_block_user(str(user_items[1]["uid"]),str(ui.BlackTimeInput.text()))
                else:
                    pass
            else:
                showmsg(MainWindow,"msg","找到了"+str(len(user_items))+"个用户？？请截图发给开发者orz"+"<br>")

def unblock_user(self):
    # print(ui.tableWidget.currentRow())
    r = ui.tableWidget.currentRow()
    if r >= 0:
        send_unblock_user(ui.tableWidget.item(r,0).text())
    else:
        showmsg(MainWindow,"error","请先选择一行再进行移除封禁！")


def send_block_user(uid,hour):
    data = "roomid="+str(bilibili().dic_bilibili['account']['roomid'])+"&block_uid="+str(uid)+"&hour="+str(hour)+"&csrf_token="+bilibili().dic_bilibili['csrf']+"&csrf="+bilibili().dic_bilibili['csrf']+"&visit_id="
    # print(data)
    url = "https://api.live.bilibili.com/banned_service/v2/Silent/add_block_user"
    response = bilibili().post_data(url,data)
    if response != False:
        data = json.loads(response.text)
        if data["code"] == 0:
            showmsg(MainWindow,"msg","封禁成功！<br><br>用户:"+str(data["data"]["uname"])+"<br>解禁时间:"+str(data["data"]["block_end_time"])+"<br>")
            ui.BlackUIDInput.setText("")
        else:
            showmsg(MainWindow,"error","错误："+str(data["code"])+"，"+str(data["message"]))
            if data["code"] == 3:
                ui.label_Login.setText("登录状态：登录已失效")

def send_unblock_user(bid):
    data = "id="+str(bid)+"&roomid="+str(bilibili().dic_bilibili['account']['roomid'])+"&csrf_token="+bilibili().dic_bilibili['csrf']+"&csrf="+bilibili().dic_bilibili['csrf']+"&visit_id="
    # print(data)
    url = "https://api.live.bilibili.com/banned_service/v1/Silent/del_room_block_user"
    response = bilibili().post_data(url,data)
    if response != False:
        data = json.loads(response.text)
        if data["code"] == 0:
            showmsg(MainWindow,"msg","解除封禁成功！<br>")
            load_blacklist()
        else:
            showmsg(MainWindow,"error","错误："+str(data["code"])+"，"+str(data["message"]))
            if data["code"] == 3:
                ui.label_Login.setText("登录状态：登录已失效")

def search_user(text):
    url = "https://api.live.bilibili.com/banned_service/v2/Silent/search_user?search="+str(text)
    response = bilibili().get_data(url)
    if response != False:
        data = json.loads(response.text)
        if data["code"] == 0:
            return data["data"]["items"]
        else:
            showmsg(MainWindow,"error","错误："+str(data["code"])+"，"+str(data["message"]))
            if data["code"] == 3:
                ui.label_Login.setText("登录状态：登录已失效")
            return False

bilibili()
app = QtWidgets.QApplication(sys.argv)
# 实例化主窗口
MainWindow = QtWidgets.QMainWindow()
ui = Ui_black.Ui_Dialog()
ui.setupUi(MainWindow)

# 实例化子窗口
child = QtWidgets.QDialog(MainWindow)
child_ui = Ui_login.Ui_dialog()
child_ui.setupUi(child)

if __name__ == "__main__":
    if bilibili().dic_bilibili['saved-session']['cookie']:
        bilibili().load_session(bilibili().dic_bilibili['saved-session'])

    ui.RoomInput.setValidator(QtGui.QIntValidator(0,999999999))
    ui.RoomInput.setText(str(bilibili().dic_bilibili['account']['roomid']))
    ui.BlackTimeInput.setValidator(QtGui.QIntValidator(1,720))
    ui.tableWidget.setColumnWidth(0,25)
    ui.tableWidget.setColumnWidth(3,128)
    ui.tableWidget.setColumnWidth(4,128)

    ui.LoginButton.clicked.connect(openlogin)
    # ui.SubmitCookieBtn.clicked.connect(button_pressed) # 未实现
    ui.RoomBtn.clicked.connect(connect_room)
    ui.refreshBtn.clicked.connect(load_blacklist)
    ui.AddBlackBtn.clicked.connect(block_user)
    ui.RemoveBlackBtn.clicked.connect(unblock_user)

    child_ui.pushButton.clicked.connect(trylogin)
    child_ui.pushButton_2.clicked.connect(reload_captcha)

    checklogin(ui=ui,pw=str(bilibili().dic_bilibili['account']['password']))

    # 显示
    MainWindow.show()

    if str(bilibili().dic_bilibili['account']['roomid']) != "":
        load_blacklist()

    sys.exit(app.exec_())