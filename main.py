# -*- coding: utf-8 -*-
import sys
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import cv2
import numpy as np
import time
import csv    #引入这个包
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets


cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
face_cascade = cv2.CascadeClassifier('F:\Python3.7\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
Id = 0

'''这个类，pyqt界面布局'''
class Ui_Dialog(object):  #qt界面
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(461, 246)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 461, 251))#571 321
        self.tabWidget.setObjectName("tabWidget")

        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 30, 171, 31))
        self.lineEdit.setText("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.lineEdit.setObjectName("lineEdit")                                                       #密码框
        self.lineEdit.setPlaceholderText('请输入6位数字密码......')

        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 120, 211, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_15 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 1, 2, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_2.addWidget(self.pushButton_13, 1, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_2.addWidget(self.pushButton_11, 0, 1, 1, 1)
        self.pushButton_43 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_43.setObjectName("pushButton_43")
        self.gridLayout_2.addWidget(self.pushButton_43, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(140, 0, 261, 31))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 70, 171, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText('提示框、文本框')

        '''str = '要显示的字符串'
        self.textEdit.setText(str)'''
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(240, 30, 54, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(240, 70, 51, 21))
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName("label_3")

        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setGeometry(QtCore.QRect(220, 110, 239, 111))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_8.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setStyleSheet("background-color:#00C78C;");######
        self.gridLayout.addWidget(self.pushButton_8, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_3.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("background-color:#00C78C;");#######
        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_5.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet("background-color:#00C78C;");
        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_9.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setStyleSheet("background-color:#00C78C;");
        self.gridLayout.addWidget(self.pushButton_9, 2, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_4.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("background-color:#00C78C;");
        self.gridLayout.addWidget(self.pushButton_4, 0, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_6.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet("background-color:#00C78C;");
        self.gridLayout.addWidget(self.pushButton_6, 1, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_10.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setStyleSheet("background-color:#00C78C;");
        self.gridLayout.addWidget(self.pushButton_10, 2, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color:#00C78C;");
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_7.setMinimumSize(QtCore.QSize(75, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setStyleSheet("background-color:#00C78C;");
        self.gridLayout.addWidget(self.pushButton_7, 1, 2, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 231, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_14 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout.addWidget(self.pushButton_14)
        self.pushButton_16 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout.addWidget(self.pushButton_16)
        self.pushButton_17 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout.addWidget(self.pushButton_19)
        self.pushButton_22 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_22.setObjectName("pushButton_22")
        self.horizontalLayout.addWidget(self.pushButton_22)
        self.pushButton_20 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_20.setObjectName("pushButton_20")
        self.horizontalLayout.addWidget(self.pushButton_20)
        self.pushButton_21 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_21.setObjectName("pushButton_21")
        self.horizontalLayout.addWidget(self.pushButton_21)
        self.pushButton_23 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_23.setObjectName("pushButton_23")
        self.horizontalLayout.addWidget(self.pushButton_23)
        self.pushButton_24 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout.addWidget(self.pushButton_24)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 201, 21))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_25 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_25.setObjectName("pushButton_25")
        self.horizontalLayout_2.addWidget(self.pushButton_25)
        self.pushButton_26 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_26.setObjectName("pushButton_26")
        self.horizontalLayout_2.addWidget(self.pushButton_26)
        self.pushButton_27 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_27.setObjectName("pushButton_27")
        self.horizontalLayout_2.addWidget(self.pushButton_27)
        self.pushButton_28 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_28.setObjectName("pushButton_28")
        self.horizontalLayout_2.addWidget(self.pushButton_28)
        self.pushButton_29 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_29.setObjectName("pushButton_29")
        self.horizontalLayout_2.addWidget(self.pushButton_29)
        self.pushButton_30 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_30.setObjectName("pushButton_30")
        self.horizontalLayout_2.addWidget(self.pushButton_30)
        self.pushButton_31 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_31.setObjectName("pushButton_31")
        self.horizontalLayout_2.addWidget(self.pushButton_31)
        self.pushButton_32 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_32.setObjectName("pushButton_32")
        self.horizontalLayout_2.addWidget(self.pushButton_32)
        self.pushButton_33 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_33.setObjectName("pushButton_33")
        self.horizontalLayout_2.addWidget(self.pushButton_33)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 90, 171, 21))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_34 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_34.setObjectName("pushButton_34")
        self.horizontalLayout_3.addWidget(self.pushButton_34)
        self.pushButton_35 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_35.setObjectName("pushButton_35")
        self.horizontalLayout_3.addWidget(self.pushButton_35)
        self.pushButton_36 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_36.setObjectName("pushButton_36")
        self.horizontalLayout_3.addWidget(self.pushButton_36)
        self.pushButton_37 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_37.setObjectName("pushButton_37")
        self.horizontalLayout_3.addWidget(self.pushButton_37)
        self.pushButton_38 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_38.setObjectName("pushButton_38")
        self.horizontalLayout_3.addWidget(self.pushButton_38)
        self.pushButton_39 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_39.setObjectName("pushButton_39")
        self.horizontalLayout_3.addWidget(self.pushButton_39)
        self.pushButton_40 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_40.setObjectName("pushButton_40")
        self.horizontalLayout_3.addWidget(self.pushButton_40)
        self.tabWidget.addTab(self.widget, "")
        self.widget_2 = QtWidgets.QWidget()
        self.widget_2.setObjectName("widget_2")
        self.pushButton_41 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_41.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_42 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_42.setGeometry(QtCore.QRect(10, 70, 75, 23))
        self.pushButton_42.setObjectName("pushButton_42")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.widget_2)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(160, 0, 293, 220)) #属性，在这里更改251 221
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(9, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 100, 141, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_44 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_44.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.pushButton_44.setObjectName("pushButton_44")#####################################
        self.tabWidget.addTab(self.widget_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        self.pushButton_2.clicked.connect(Dialog.on_push_button_click)  ####
        self.pushButton_3.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_4.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_5.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_6.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_7.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_8.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_9.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_10.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_11.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_12.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_13.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_14.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_15.clicked.connect(Dialog.on_push_button_click)  ########
        self.pushButton.clicked.connect(Dialog.on_push_button_click)  # 确认键
        self.pushButton_16.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_17.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_18.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_19.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_20.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_21.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_22.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_23.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_24.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_25.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_26.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_27.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_28.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_29.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_30.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_31.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_32.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_33.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_34.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_35.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_36.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_37.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_38.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_39.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_40.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_41.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_42.clicked.connect(Dialog.on_push_button_click)  #给按键添加槽
        self.pushButton_43.clicked.connect(Dialog.on_push_button_click)
        self.pushButton_44.clicked.connect(Dialog.on_push_button_click)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.pushButton_4, self.pushButton_3)
        Dialog.setTabOrder(self.pushButton_3, self.pushButton)
        Dialog.setTabOrder(self.pushButton, self.pushButton_5)
        Dialog.setTabOrder(self.pushButton_5, self.pushButton_6)
        Dialog.setTabOrder(self.pushButton_6, self.pushButton_7)
        Dialog.setTabOrder(self.pushButton_7, self.pushButton_8)
        Dialog.setTabOrder(self.pushButton_8, self.pushButton_9)
        Dialog.setTabOrder(self.pushButton_9, self.pushButton_2)
        Dialog.setTabOrder(self.pushButton_2, self.pushButton_10)
        Dialog.setTabOrder(self.pushButton_10, self.pushButton_11)
        Dialog.setTabOrder(self.pushButton_11, self.pushButton_12)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "智能门锁界面"))
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.tabWidget.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("G:\pyqt\kl.jpg")))
        self.setPalette(window_pale)  #背景


        self.pushButton_15.setText(_translate("Dialog", "取消"))
        self.pushButton.setText(_translate("Dialog", "确认"))
        self.pushButton_12.setText(_translate("Dialog", "修改密码"))
        self.pushButton_13.setText(_translate("Dialog", "删除指纹用户"))
        self.pushButton_11.setText(_translate("Dialog", "添加指纹用户"))
        self.pushButton_43.setText(_translate("Dialog", "删除用户信息"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">欢迎使用智能门锁系统</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "密码框："))
        self.label_3.setText(_translate("Dialog", "文本框："))

        self.pushButton_8.setText(_translate("Dialog", "7"))
        self.pushButton_3.setText(_translate("Dialog", "2"))
        self.pushButton_5.setText(_translate("Dialog", "4"))
        self.pushButton_9.setText(_translate("Dialog", "8"))
        self.pushButton_4.setText(_translate("Dialog", "3"))
        self.pushButton_6.setText(_translate("Dialog", "5"))
        self.pushButton_10.setText(_translate("Dialog", "9"))
        self.pushButton_2.setText(_translate("Dialog", "1"))
        self.pushButton_7.setText(_translate("Dialog", "6"))
        self.pushButton_14.setText(_translate("Dialog", "q"))
        self.pushButton_16.setText(_translate("Dialog", "w"))
        self.pushButton_17.setText(_translate("Dialog", "e"))
        self.pushButton_18.setText(_translate("Dialog", "r"))
        self.pushButton_19.setText(_translate("Dialog", "t"))
        self.pushButton_22.setText(_translate("Dialog", "y"))
        self.pushButton_20.setText(_translate("Dialog", "u"))
        self.pushButton_21.setText(_translate("Dialog", "i"))
        self.pushButton_23.setText(_translate("Dialog", "o"))
        self.pushButton_24.setText(_translate("Dialog", "p"))
        self.pushButton_25.setText(_translate("Dialog", "a"))
        self.pushButton_26.setText(_translate("Dialog", "s"))
        self.pushButton_27.setText(_translate("Dialog", "d"))
        self.pushButton_28.setText(_translate("Dialog", "f"))
        self.pushButton_29.setText(_translate("Dialog", "g"))
        self.pushButton_30.setText(_translate("Dialog", "h"))
        self.pushButton_31.setText(_translate("Dialog", "j"))
        self.pushButton_32.setText(_translate("Dialog", "k"))
        self.pushButton_33.setText(_translate("Dialog", "l"))
        self.pushButton_34.setText(_translate("Dialog", "z"))
        self.pushButton_35.setText(_translate("Dialog", "x"))
        self.pushButton_36.setText(_translate("Dialog", "c"))
        self.pushButton_37.setText(_translate("Dialog", "v"))
        self.pushButton_38.setText(_translate("Dialog", "b"))
        self.pushButton_39.setText(_translate("Dialog", "n"))
        self.pushButton_40.setText(_translate("Dialog", "m"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Dialog", "主页"))
        self.pushButton_41.setText(_translate("Dialog", "开始检测"))
        self.pushButton_42.setText(_translate("Dialog", "录入用户"))
        self.label_5.setText(_translate("Dialog", "视频显示"))
        self.pushButton_44.setText(_translate("Dialog", "退出检测"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget_2), _translate("Dialog", "人脸检测"))

'''这个类，将人脸识别和pyqt界面链接起来....'''
class System(QMainWindow , Ui_Dialog):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_Dialog.__init__(self)
        Face_process.__init__(self)
        self.setupUi(self)
        self.initUI()
        self.aa = 0
        self.bb = 0
        self.cc = 0
        self.timer_camera = QtCore.QTimer(self)  #定时器模块 初始化
        self.timer_camera.timeout.connect(self.show_plc)  #连接槽函数
        self.timer_camera.start(10)              #计时并启动
        Face_process.sd = self.label_5
        Face_process.ass = self.timer_camera
        Face_process.zuiz = self.cc

    def show_plc(self):#槽函数定时显示，将摄像头的数据显示出来
        success , frame2 = cap.read()
        print(frame2.shape)
        if success:
            frame2 = cv2.resize(frame2,(320,240) , interpolation=cv2.INTER_LINEAR)
            show = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
            showlmage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
            self.label_5.setPixmap(QtGui.QPixmap.fromImage(showlmage))
            self.timer_camera.start(10)
    def slotstart(self):
        self.timer_camera.start(10)  # 计时并启动
        self.timer_camera.timeout.connect(self.show_plc)  # 连接槽函数

    def slotstop(self):
        self.timer_camera.stop()

    def initUI(self):
        self.show()

    def on_push_button_click(self, Dialog):  # 不能放在里面Ui_Dialog里面
        sender = self.sender()
        if sender.text() =='开始检测':
            try:
                self.lineEdit_3.setPlaceholderText('正在检测！！多角度')
                Face_process.face_distinguish()
                self.lineEdit_3.setPlaceholderText('检测结束')
                #cap.release()
            except:
                self.lineEdit_3.setPlaceholderText('没录入用户面部信息')
        elif sender.text() == '确认':

            if self.aa == 1:
                namess = self.lineEdit_2.text()
                print(namess)
                self.aa = 0
                path = 'G:\pyqt\yonghu.csv'
                with open(path, 'a+', encoding='utf-8', newline='') as f:
                    csv_write = csv.writer(f)
                    date_row = [namess]
                    csv_write.writerow(date_row)
                    self.lineEdit_2.setText('')
                    self.lineEdit_2.setPlaceholderText('正在录入...')
                    self.lineEdit_3.setPlaceholderText('正在录入，尽可能多角度。')
                    Face_process.generate()
                    self.lineEdit_3.setText('')
                    self.lineEdit_3.setPlaceholderText('录入结束！')
                    self.lineEdit_2.setText('')
                    self.lineEdit_2.setPlaceholderText('录入结束。')
                    self.lineEdit.setText('')
                    #cap.release()
                    cv2.destroyAllWindows()
            elif self.aa == 2:                                 #####需要检验密码。。。。。。。。。。。。
                self.aa =0
                f = open('G:\pyqt\yonghu.csv' , 'r')           #密码文件
                fd = csv.reader(f)
                ff = list(fd)
                print(ff[0][1])
                if ff[0][1] == self.lineEdit.text():          #####密码正确
                    if self.bb == 1:
                        self.lineEdit_2.setText('请输入新的密码')
                        self.lineEdit.setText('')
                        self.aa = 3
                        self.bb = 0
                    elif self.bb == 2:
                        self.bb = 0
                        try:
                            os.remove('G:\pyqt\ja.csv')
                            fg = open('G:\pyqt\yonghu.csv', 'r')
                            gh = csv.reader(fg)
                            line = list(gh)
                            str1 = line[0]
                            print(str1)
                            list1 = os.listdir('G:\pyqt\my_user')
                            for line in list1:
                                os.remove('G:\pyqt\my_user' + os.sep + line)  # 把照片全部清除
                            jkj = open('G:\pyqt\yonghu.csv', 'w', encoding='utf-8', newline='')
                            write_csv = csv.writer(jkj)
                            row = str1
                            write_csv.writerow(row)
                            # write_csv.close()
                            self.lineEdit_2.setText('删除面部数据成功！')
                            self.lineEdit.setText('')
                        except:
                            self.lineEdit_2.setText('无存在数据，请确认！！')
                    elif self.bb == 3:
                        self.bb = 0
                        print('录入指纹')
                    elif self.bb == 4:
                        self.bb = 0
                        print('选择要删除的用户')
                    elif self.bb == 5:
                        self.bb = 0
                        self.lineEdit_3.setPlaceholderText('添加用户名!!!')
                        self.lineEdit_2.setText('')
                        self.lineEdit_2.setPlaceholderText('添加用户名!!!')
                        self.aa = 1
                else:
                    if self.bb == 1:
                        self.bb = 0
                        self.lineEdit_2.setText('错误，请重新开始，点击‘修改密码’')
                        self.lineEdit.setText('')
                    elif self.bb == 2:
                        self.bb = 0
                        self.lineEdit_2.setText('密码错误！！！')
                        self.lineEdit.setText('')
            elif self.aa == 3:              #密码正确之后的操作  修改密码
                self.aa = 0
                new_mima = self.lineEdit.text()
                f = open('G:\pyqt\yonghu.csv','r')
                ff = csv.reader(f)
                fff = list(ff)
                fff[0][1] = new_mima
                with open('G:\pyqt\yonghu.csv', 'w' ,encoding='utf-8',newline='') as f:       #修改密码
                    csv_write = csv.writer(f)
                    for i in fff:
                        date_row = i
                        csv_write.writerow(date_row)
                self.lineEdit_2.setText('修改密码成功！！')
                self.lineEdit.setText('')
            else:                                                 #密码锁、检验密码
                path = 'G:\pyqt\yonghu.csv'                       #密码文件
                with open(path, 'r') as f:
                    csv_read = csv.reader(f)
                    line = list(csv_read)
                    if (line[0][1]) == self.lineEdit.text():#读取csv文件中的密码
                        self.lineEdit_2.setText('密码正确，开锁~')
                        self.lineEdit.setText('')
                    else:
                        self.lineEdit_2.setText('密码错误，请重试！！')
                        self.lineEdit.setText('')

        elif sender.text() == '添加指纹用户':
            self.lineEdit.setText('')
            self.lineEdit_2.setText('请输入用户密码')
            self.aa = 2
            self.bb = 3
            print('添加指纹用户')
        elif sender.text() == '录入用户':
            self.lineEdit.setText('')
            self.lineEdit_2.setText('请输入用户密码')
            self.lineEdit_3.setPlaceholderText('请输入用户密码!!!')
            #self.lineEdit_2.setPlaceholderText('添加用户名!!!')
            self.aa = 2
            self.bb = 5
        elif sender.text() == '取消':
            self.aa = 0
            self.bb = 0
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            self.lineEdit_3.setText('')
            print('取消')
        elif sender.text() == '修改密码':
            self.aa = 2
            self.bb = 1
            self.lineEdit_2.setText('请输入旧密码')
        elif sender.text() == '删除指纹用户':
            self.aa = 2
            self.bb = 4
            self.lineEdit_2.setText('请输入用户密码')
            print('删除指纹用户')
        elif sender.text() == '删除用户信息':                                         #删除多个文件
            self.lineEdit_2.setText('请输入用户密码！！')
            self.aa = 2
            self.bb = 2
        elif sender.text() == '退出检测':
            self.cc = 1
            Face_process.zuiz = self.cc
            print('退出检测')


        elif ord(sender.text())>=49 and ord(sender.text())<=57 :
            gg = self.lineEdit.text()
            self.lineEdit.setText(gg + sender.text())
            #print(sender.text())
        else:
            ss = self.lineEdit_2.text()
            self.lineEdit_2.setText(ss+sender.text())

'''脸部识别的类'''
class Face_process():
    def __init__(self):
        #super().__init__(self.label_5)
        self.sd = 0
        self.ass = 0
        self.zuiz = 1
        print('kjdbgfbkjasdhfkj')
    def detect(filename):#静态人脸检测
        img = cv2.imread(filename)
        gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray , 1.3 , 5)
        for (x , y, w, h) in faces:
            img = cv2.rectangle(img, (x, y) , (x+w , y+h) , (0,0,255) , 2)
        cv2.namedWindow('get_face')
        cv2.imshow('get_face',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def video_face_detect():#视频人脸检测

        while True:
            ret, frame = cap.read()
            #img = cv2.imread(frame)
            frame1 = frame.copy()  #图像拷贝
            gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray , 1.3 , 5)
            for (x , y , w, h) in faces:
                img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            #cv2.namedWindow('after_detect')
            img1 = np.hstack((frame1 , img))
            cv2.imshow('after_detect',img1)
            if cv2.waitKey(1) == ord('c'):
                break

    def generate():                                          #2020.4.9已测试成功可以用
        counts = 1
        path1 = 'G:\pyqt\my_user'
        files = os.listdir(path1)
        count,nums = 1,0
        for filename in files:#计算文件夹中有多少个pgm文件 ，比较灵活点
            count += 1
            nums +=1
        Id = nums/200

        print('开始录入用户脸部信息！请摘掉眼镜........')
        print('不要固定的表情。。。。')
        Face_process.ass.stop()                                    #关闭定时器
        while True:
            ret , frame = cap.read()
            gray = cv2.cvtColor( frame , cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale( gray , 1.3 , 5 )
            for (x , y , w , h) in faces:
                img = cv2.rectangle(frame , (x, y) , (x+w,y+h) , (0,0,255) , 3)
                after = cv2.resize(gray[y:y+h,x:x+w] , (200 , 200))  #调整图片规格
                cv2.imwrite('G:\pyqt\my_user\%s.pgm' %str(count) , after)
                Csv_file.write_csv(('my_user\%s.pgm'%str(count)) , Id)  #####################################################
                print('已录入' + str(counts) + '张图像....')
                cv2.putText(img,str(counts) + 'pictures have been entered...',(10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),3)
                count += 1
                counts += 1

            #cv2.namedWindow('camera')
            #print(frame.shape)

            frame = cv2.resize(frame,(320,240) , interpolation=cv2.INTER_LINEAR)
            show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            showlmage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888) #这里把cv图像的格式，转换成Qimage图像格式
            Face_process.sd.setPixmap(QtGui.QPixmap.fromImage(showlmage))                                 #在界面中显示视频图片


            #cv2.imshow('camera' , frame)
            cv2.waitKey(80)  #延时500毫秒
            if counts > 200:   #录入20张照片
                print('录入结束！')
                Face_process.ass.start(10)#开启定时器
                break

    def read_images(path):
        c = 0
        x,y = [] , []
        with open(path , 'r+') as f:
            csv_read = csv.reader(f)
            for line in csv_read:
                im = cv2.imread(str('G:\pyqt' + os.sep + line[0]), cv2.IMREAD_GRAYSCALE)
                x.append(np.asarray(im, dtype=np.uint8))
                y.append(line[1])
        return [x ,y]

    def face_distinguish():
        names = []
        f = open('G:\pyqt\yonghu.csv' , 'r+')
        csv_read = csv.reader(f)
        for name in csv_read:
            names.append(name[0])

        print((names))
        [x , y] = Face_process.read_images('G:\pyqt\ja.csv') #加载图片
        y = np.asarray(y , dtype=np.int32)
        Face_process.ass.stop()                                                        #关闭定时器，不显示图像
        Face_process.sd.setPixmap(QtGui.QPixmap(""))                                   #模型训练时需要一段事件，将最后卡顿是照片清理掉。。
        Face_process.sd.setText('系统正在工作，请耐心等候........')
        cv2.waitKey(1)                                                                 #延时一毫秒才有效果
        model = cv2.face.LBPHFaceRecognizer_create()                                   #人脸识别模型c
        model.train(np.asarray(x) , np.asarray(y))                                     #训练模型
        #face_cascade = cv2.CascadeClassifier('F:/Python3.7/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')  #加载人脸检测级联分类器
        while True:
            read , img = cap.read()                                                    #读取摄像头信息
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)                                #灰度化
            faces = face_cascade.detectMultiScale(gray, 1.3 , 5)                       #人脸检测
            for (x,y,w,h) in faces:
                img = cv2.rectangle(img , (x , y) , (x+w , y+h) , (0,0,255) , 3)       #画框
                roi = gray[x:x+w , y:y+h]                                              #扣出人脸图
                try:
                    roi = cv2.resize(roi,(200,200) , interpolation=cv2.INTER_LINEAR)   #图像规格大小调整
                    params = model.predict(roi)                                        #预测、识别
                    if params[1]<=50:
                        print('label:%s,confidence:%.2f' % (params[0], params[1]))  # 打印识别信息
                        cv2.putText(img, names[params[0]+1], (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),3)  # 贴标签
                except:
                    continue
            '''cv2.namedWindow('camera')
            cv2.imshow('camera' , img)'''
            img = cv2.resize(img, (320, 240), interpolation=cv2.INTER_LINEAR)    #调整图像规格
            show = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)                          #调整图像颜色通道
            showlmage = QtGui.QImage(show.data, show.shape[1], show.shape[0],QtGui.QImage.Format_RGB888)  # 这里把cv图像的格式，转换成Qimage图像格式
            Face_process.sd.setPixmap(QtGui.QPixmap.fromImage(showlmage))
            cv2.waitKey(1)
            print(Face_process.zuiz)
            #print(System.cc)
            if Face_process.zuiz == 1:                                        #退出检测
                Face_process.zuiz = 0
                Face_process.ass.start(10)                                    #开始定时器
                break

class Csv_file():
    def create_csv():
        path = 'G:\pyqt\ja.csv'
        with open(path , 'w' , encoding= 'utf-8' , newline='') as f:#open(path,'w')返回的值给f
            csv_write = csv.writer(f)
            csv_head = ['good' , 1]
            csv_write.writerow(csv_head)
    def write_csv(filename,user_id):
        path = 'G:\pyqt\ja.csv'
        with open(path , 'a+',encoding= 'utf-8' , newline='') as f:
            csv_write = csv.writer(f)
            date_row = [filename,int(user_id)]
            csv_write.writerow(date_row)
    def read_csv(path):
        #path = 'G:\pyqt\ja.csv'
        with open(path , 'r') as f:
            csv_read = csv.reader(f)
            return csv_read



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = System()
    sys.exit(app.exec_())






