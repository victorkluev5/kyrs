# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'people.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class Admin(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 493)
        MainWindow.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 491, 431))
        self.tableView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableView.setObjectName("tableView")
        self.btn_people_up = QtWidgets.QPushButton(self.centralwidget)
        self.btn_people_up.setGeometry(QtCore.QRect(570, 40, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_people_up.setFont(font)
        self.btn_people_up.setStyleSheet("background-color: rgb(143, 240, 164);")
        self.btn_people_up.setObjectName("btn_people_up")
        self.btn_people_del = QtWidgets.QPushButton(self.centralwidget)
        self.btn_people_del.setGeometry(QtCore.QRect(570, 130, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_people_del.setFont(font)
        self.btn_people_del.setStyleSheet("background-color: rgb(246, 97, 81)")
        self.btn_people_del.setObjectName("btn_people_del")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(680, 400, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet("background-color: rgb(246, 97, 81);")
        self.btn_exit.setObjectName("btn_exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
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
        self.btn_people_up.setText(_translate("MainWindow", "Добавление сотрудника"))
        self.btn_people_del.setText(_translate("MainWindow", "Удаление сотрудника"))
        self.btn_exit.setText(_translate("MainWindow", "Выход"))
