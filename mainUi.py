# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(894, 507)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QtCore.QSize(0, 0))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chose_btn = QtWidgets.QToolButton(self.centralwidget)
        self.chose_btn.setGeometry(QtCore.QRect(770, 19, 41, 21))
        self.chose_btn.setObjectName("chose_btn")
        self.img_path = QtWidgets.QComboBox(self.centralwidget)
        self.img_path.setGeometry(QtCore.QRect(510, 19, 251, 21))
        self.img_path.setObjectName("img_path")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 20, 71, 20))
        self.label.setObjectName("label")
        self.img_show = QtWidgets.QLabel(self.centralwidget)
        self.img_show.setGeometry(QtCore.QRect(90, 80, 300, 300))
        self.img_show.setAutoFillBackground(True)
        self.img_show.setText("")
        self.img_show.setPixmap(QtGui.QPixmap("E:/Picture/Black Gooooogle.png"))
        self.img_show.setObjectName("img_show")
        self.img_show2 = QtWidgets.QLabel(self.centralwidget)
        self.img_show2.setGeometry(QtCore.QRect(500, 80, 300, 300))
        self.img_show2.setAutoFillBackground(True)
        self.img_show2.setText("")
        self.img_show2.setPixmap(QtGui.QPixmap("E:/Picture/Black Gooooogle.png"))
        self.img_show2.setObjectName("img_show2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 210, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.url_text = QtWidgets.QLineEdit(self.centralwidget)
        self.url_text.setGeometry(QtCore.QRect(80, 20, 321, 20))
        self.url_text.setObjectName("url_text")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 51, 20))
        self.label_2.setObjectName("label_2")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(610, 410, 91, 41))
        self.save_btn.setObjectName("save_btn")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(420, 100, 41, 41))
        self.commandLinkButton.setText("")
        self.commandLinkButton.setIconSize(QtCore.QSize(80, 80))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(560, 50, 181, 16))
        self.label_3.setObjectName("label_3")
        self.tips = QtWidgets.QLabel(self.centralwidget)
        self.tips.setEnabled(False)
        self.tips.setGeometry(QtCore.QRect(100, 430, 301, 16))
        self.tips.setText("")
        self.tips.setObjectName("tips")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python快速抠图"))
        self.chose_btn.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "本地图片选择"))
        self.pushButton.setText(_translate("MainWindow", "抠图"))
        self.label_2.setText(_translate("MainWindow", "网络图片："))
        self.save_btn.setText(_translate("MainWindow", "保存"))
        self.label_3.setText(_translate("MainWindow", "（提示：文件最大不能超过8MB）"))

