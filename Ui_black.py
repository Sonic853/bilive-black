# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\HTTP\Git\bilive-black\black.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 490)
        Dialog.setMinimumSize(QtCore.QSize(650, 490))
        Dialog.setMaximumSize(QtCore.QSize(650, 490))
        self.CookieInput = QtWidgets.QLineEdit(Dialog)
        self.CookieInput.setGeometry(QtCore.QRect(89, 10, 470, 30))
        self.CookieInput.setObjectName("CookieInput")
        self.SubmitCookieBtn = QtWidgets.QPushButton(Dialog)
        self.SubmitCookieBtn.setGeometry(QtCore.QRect(570, 10, 70, 30))
        self.SubmitCookieBtn.setObjectName("SubmitCookieBtn")
        self.AddBlackBtn = QtWidgets.QPushButton(Dialog)
        self.AddBlackBtn.setGeometry(QtCore.QRect(540, 450, 100, 30))
        self.AddBlackBtn.setObjectName("AddBlackBtn")
        self.RemoveBlackBtn = QtWidgets.QPushButton(Dialog)
        self.RemoveBlackBtn.setGeometry(QtCore.QRect(540, 90, 100, 30))
        self.RemoveBlackBtn.setObjectName("RemoveBlackBtn")
        self.refreshBtn = QtWidgets.QPushButton(Dialog)
        self.refreshBtn.setGeometry(QtCore.QRect(540, 130, 100, 30))
        self.refreshBtn.setObjectName("refreshBtn")
        self.BlackUIDInput = QtWidgets.QLineEdit(Dialog)
        self.BlackUIDInput.setGeometry(QtCore.QRect(90, 410, 550, 30))
        self.BlackUIDInput.setObjectName("BlackUIDInput")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 410, 80, 30))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.BlackTimeInput = QtWidgets.QLineEdit(Dialog)
        self.BlackTimeInput.setGeometry(QtCore.QRect(370, 450, 130, 30))
        self.BlackTimeInput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.BlackTimeInput.setObjectName("BlackTimeInput")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(230, 450, 130, 30))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(510, 450, 20, 30))
        self.label_4.setObjectName("label_4")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 520, 310))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.LoginButton = QtWidgets.QPushButton(Dialog)
        self.LoginButton.setGeometry(QtCore.QRect(10, 10, 70, 30))
        self.LoginButton.setObjectName("LoginButton")
        self.RoomInput = QtWidgets.QLineEdit(Dialog)
        self.RoomInput.setGeometry(QtCore.QRect(10, 50, 550, 30))
        self.RoomInput.setObjectName("RoomInput")
        self.RoomBtn = QtWidgets.QPushButton(Dialog)
        self.RoomBtn.setGeometry(QtCore.QRect(570, 50, 70, 30))
        self.RoomBtn.setObjectName("RoomBtn")
        self.label_Login = QtWidgets.QLabel(Dialog)
        self.label_Login.setGeometry(QtCore.QRect(10, 450, 180, 30))
        self.label_Login.setObjectName("label_Login")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "房管封禁助手"))
        self.SubmitCookieBtn.setText(_translate("Dialog", "提交Cookie"))
        self.AddBlackBtn.setText(_translate("Dialog", "添加封禁"))
        self.RemoveBlackBtn.setText(_translate("Dialog", "移除封禁"))
        self.refreshBtn.setText(_translate("Dialog", "刷新列表"))
        self.label.setText(_translate("Dialog", "用户名/UID："))
        self.label_3.setText(_translate("Dialog", "封禁时间："))
        self.label_4.setText(_translate("Dialog", "时"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "用户名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "用户ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "封禁时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "解封时间"))
        self.LoginButton.setText(_translate("Dialog", "使用登录"))
        self.RoomBtn.setText(_translate("Dialog", "连接房间"))
        self.label_Login.setText(_translate("Dialog", "登录状态：未登录"))