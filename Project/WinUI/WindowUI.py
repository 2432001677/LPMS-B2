# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1098, 394)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView_swims = QtWidgets.QListView(self.centralwidget)
        self.listView_swims.setGeometry(QtCore.QRect(20, 20, 281, 311))
        self.listView_swims.setObjectName("listView_swims")
        self.bt_summary = QtWidgets.QPushButton(self.centralwidget)
        self.bt_summary.setGeometry(QtCore.QRect(970, 20, 101, 41))
        self.bt_summary.setObjectName("bt_summary")
        self.bt_detail = QtWidgets.QPushButton(self.centralwidget)
        self.bt_detail.setGeometry(QtCore.QRect(970, 150, 101, 41))
        self.bt_detail.setObjectName("bt_detail")
        self.bt_quit = QtWidgets.QPushButton(self.centralwidget)
        self.bt_quit.setGeometry(QtCore.QRect(970, 290, 101, 41))
        self.bt_quit.setObjectName("bt_quit")
        self.tableView_detail = QtWidgets.QTableView(self.centralwidget)
        self.tableView_detail.setEnabled(True)
        self.tableView_detail.setGeometry(QtCore.QRect(330, 20, 331, 311))
        self.tableView_detail.setObjectName("tableView_detail")
        self.frame_sum = QtWidgets.QFrame(self.centralwidget)
        self.frame_sum.setEnabled(True)
        self.frame_sum.setGeometry(QtCore.QRect(330, 20, 581, 311))
        self.frame_sum.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sum.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sum.setObjectName("frame_sum")
        self.label_main_swim = QtWidgets.QLabel(self.frame_sum)
        self.label_main_swim.setGeometry(QtCore.QRect(30, 30, 91, 41))
        self.label_main_swim.setObjectName("label_main_swim")
        self.text_main_swim = QtWidgets.QLabel(self.frame_sum)
        self.text_main_swim.setGeometry(QtCore.QRect(30, 90, 91, 41))
        self.text_main_swim.setObjectName("text_main_swim")
        self.table_summary_time = QtWidgets.QLabel(self.frame_sum)
        self.table_summary_time.setGeometry(QtCore.QRect(170, 30, 101, 41))
        self.table_summary_time.setObjectName("table_summary_time")
        self.summary_time = QtWidgets.QTimeEdit(self.frame_sum)
        self.summary_time.setGeometry(QtCore.QRect(170, 90, 101, 41))
        self.summary_time.setTime(QtCore.QTime(5, 5, 8))
        self.summary_time.setObjectName("summary_time")
        self.label_calorie = QtWidgets.QLabel(self.frame_sum)
        self.label_calorie.setEnabled(False)
        self.label_calorie.setGeometry(QtCore.QRect(310, 30, 81, 41))
        self.label_calorie.setObjectName("label_calorie")
        self.label_calorie_num = QtWidgets.QLabel(self.frame_sum)
        self.label_calorie_num.setGeometry(QtCore.QRect(310, 90, 81, 41))
        self.label_calorie_num.setObjectName("label_calorie_num")
        self.label_average_speed = QtWidgets.QLabel(self.frame_sum)
        self.label_average_speed.setGeometry(QtCore.QRect(450, 30, 81, 41))
        self.label_average_speed.setObjectName("label_average_speed")
        self.label_average_speed_num = QtWidgets.QLabel(self.frame_sum)
        self.label_average_speed_num.setGeometry(QtCore.QRect(450, 90, 81, 41))
        self.label_average_speed_num.setObjectName("label_average_speed_num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1098, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_summary.setText(_translate("MainWindow", "概览"))
        self.bt_detail.setText(_translate("MainWindow", "详情"))
        self.bt_quit.setText(_translate("MainWindow", "退出"))
        self.label_main_swim.setText(_translate("MainWindow", "主泳姿"))
        self.text_main_swim.setText(_translate("MainWindow", "自由泳"))
        self.table_summary_time.setText(_translate("MainWindow", "时间"))
        self.label_calorie.setText(_translate("MainWindow", "能量消耗"))
        self.label_calorie_num.setText(_translate("MainWindow", "8千卡"))
        self.label_average_speed.setText(_translate("MainWindow", "平均配速"))
        self.label_average_speed_num.setText(_translate("MainWindow", "12\'\'"))
