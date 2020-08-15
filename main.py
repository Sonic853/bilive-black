import Ui_black,Ui_login,sys
from login import login
from PyQt5 import QtCore, QtGui, QtWidgets
from bilibili import bilibili
# from PyQt5.QtWidgets import QApplication, QMainWindow

def button_pressed(self):
    print('Button pressed')

def button_pressed2(self):
    text = child_ui.lineEdit_u.text()
    print('Button pressed: '+text)

def showerror(error):
    msg = QtWidgets.QMessageBox()
    # msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setText("错误")
    msg.setInformativeText(error)
    msg.setWindowTitle("Error")
    msg.exec_()

def checklogin(ui,pw):
    if pw == "":
        ui.label_Login.setText("登录状态：未登录")
    else:
        ui.label_Login.setText("登录状态：已登录")

def trylogin(self):
    if str(child_ui.lineEdit_u.text()) == "" or str(child_ui.lineEdit_p.text()) == "" :
        showerror('用户名和密码不能为空！')
    else:
        trytext = login().loginup(username=str(child_ui.lineEdit_u.text()),password=str(child_ui.lineEdit_p.text()))
        if trytext != True:
            showerror(trytext)
        else:
            pass



bilibili()
app = QtWidgets.QApplication(sys.argv)
# 实例化主窗口
MainWindow = QtWidgets.QMainWindow()
ui = Ui_black.Ui_Dialog()
ui.setupUi(MainWindow)

# 实例化子窗口
child = QtWidgets.QDialog()
child_ui = Ui_login.Ui_dialog()
child_ui.setupUi(child)

if __name__ == "__main__":
    
    ui.LoginButton.clicked.connect(child.show)
    ui.SubmitCookieBtn.clicked.connect(button_pressed)

    child_ui.pushButton.clicked.connect(trylogin)

    checklogin(ui=ui,pw=str(bilibili().dic_bilibili['account']['password']))

    # 显示
    MainWindow.show()
    sys.exit(app.exec_())