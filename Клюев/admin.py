# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'okno.ui'
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
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(181, 131, 90)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 251, 51))
        self.label.setObjectName("label")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(40, 80, 371, 371))
        self.tableView.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.tableView.setObjectName("tableView")
        self.tableView.setColumnWidth(1, 100)
        self.label_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_0.setGeometry(QtCore.QRect(310, 30, 21, 31))
        self.label_0.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 80, 171, 41))
        self.pushButton.setStyleSheet("font: 12pt \"Open Sans\";\n"
"background-color:rgb(205, 171, 143)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 150, 171, 41))
        self.pushButton_2.setStyleSheet("font: 12pt \"Open Sans\";\n"
"background-color: rgb(205, 171, 143)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(640, 500, 121, 41))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_del = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_del.setGeometry(QtCore.QRect(580, 220, 171, 41))
        self.pushButton_del.setStyleSheet("font: 12pt \"Open Sans\";\n"
"background-color: rgb(205, 171, 143)")
        self.pushButton_del.setObjectName("pushButton_del")
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Общий доход компании:</span></p></body></html>"))
        self.label_0.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">0</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Добавить Доход"))
        self.pushButton_2.setText(_translate("MainWindow", "Расчитать прибыль"))
        self.pushButton_exit.setText(_translate("MainWindow", "Выход"))
        self.pushButton_del.setText(_translate("MainWindow", "Удалить"))
