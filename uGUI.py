# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1282, 902)
        MainWindow.setStyleSheet("#centralwidget{background-image: url(:/background_and_logo/004.png);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.video = QtWidgets.QLabel(self.centralwidget)
        self.video.setGeometry(QtCore.QRect(0, 130, 1280, 720))
        self.video.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.video.setObjectName("video")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 20, 111, 81))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/background_and_logo/003.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.btn_ext = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ext.setGeometry(QtCore.QRect(1140, 20, 121, 41))
        self.btn_ext.setObjectName("btn_ext")
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(960, 20, 121, 41))
        self.btn_open.setObjectName("btn_open")
        self.btn_open_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_2.setGeometry(QtCore.QRect(790, 20, 121, 41))
        self.btn_open_2.setObjectName("btn_open_2")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(870, 80, 121, 41))
        self.btn_stop.setObjectName("btn_stop")
        self.btn_ok = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ok.setGeometry(QtCore.QRect(1060, 80, 121, 41))
        self.btn_ok.setObjectName("btn_ok")
        self.logo2 = QtWidgets.QLabel(self.centralwidget)
        self.logo2.setGeometry(QtCore.QRect(160, 20, 561, 101))
        self.logo2.setText("")
        self.logo2.setPixmap(QtGui.QPixmap(":/background_and_logo/logo2.png"))
        self.logo2.setScaledContents(True)
        self.logo2.setObjectName("logo2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1282, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AI智能训练师"))
        self.video.setText(_translate("MainWindow", "TextLabel"))
        self.btn_ext.setText(_translate("MainWindow", "退出程序"))
        self.btn_open.setText(_translate("MainWindow", "打开视频"))
        self.btn_open_2.setText(_translate("MainWindow", "打开照片"))
        self.btn_stop.setText(_translate("MainWindow", "暂停视频"))
        self.btn_ok.setText(_translate("MainWindow", "恢复播放"))

