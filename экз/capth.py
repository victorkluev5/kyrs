from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import random
from PyQt5.QtCore import *

class Captcha(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(232, 265)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(153, 193, 241)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(191, 64, 64, 0);\n"
"font: 10pt \"Open Sans\";")
        self.label.setObjectName("label")
        self.label_Kapcha = QtWidgets.QLabel(self.centralwidget)
        self.label_Kapcha.setGeometry(QtCore.QRect(90, 80, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(10)
        font.setStrikeOut(True)
        self.label_Kapcha.setFont(font)
        self.label_Kapcha.setMouseTracking(False)
        self.label_Kapcha.setStyleSheet("font: 81 11pt \"Open Sans\";")
        self.label_Kapcha.setObjectName("label_Kapcha")
        self.lineEdit_kapcha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_kapcha.setGeometry(QtCore.QRect(40, 110, 151, 26))
        font = QtGui.QFont()
        font.setFamily("MathJax_Script")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_kapcha.setFont(font)
        self.lineEdit_kapcha.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.lineEdit_kapcha.setObjectName("lineEdit_kapcha")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(60, 200, 101, 26))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("font: 10pt \"Open Sans\";\n"
                                        "background-color: rgb(143, 240, 164)")
        self.pushButton_1.setObjectName("pushButton")
        self.label_Time = QtWidgets.QLabel(self.centralwidget)
        self.label_Time.setGeometry(QtCore.QRect(70, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_Time.setFont(font)
        self.label_Time.setStyleSheet("font: 11pt \"Open Sans\";")
        self.label_Time.setObjectName("label_Time")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Введите капчу:</span></p></body></html>"))
        self.label_Kapcha.setText(_translate("MainWindow", "54567"))
        self.pushButton_1.setText(_translate("MainWindow", "Проверить"))
        self.label_Time.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))


        self.setWindowFlags(Qt.FramelessWindowHint)
        self.label_Kapcha.setText(str(random.randint(1000,9000)))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        
        self.timer = QTimer()
        self.count = 10
        self.label_Time.setText(str(self.count))
        self.timer.timeout.connect(self.timer_tick)
        
        self.pushButton_1.clicked.connect(self.ver)
        
    
    def ver (self):
            
        
        if self.lineEdit_kapcha.text() == self.label_Kapcha.text():
            QMessageBox.information(self, "Успех", "Успешно")
            self.close()
            
            
        else:
            self.lineEdit_kapcha.setDisabled(True)
            self.timer.start()
            QMessageBox.critical(self, "error", "Введено неправильно")
            self.timer_tick()
            
            
        
            
    def timer_tick(self):
        self.timer.start(1000)
        self.count -=1
        self.label_Time.setText(str(self.count))
        
        if  self.count == 0:
            self.timer.stop()
            self.count =10
            self.lineEdit_kapcha.setDisabled(False)