import sys
from PyQt5 import QtCore
from PyQt5.QtSql import QSqlDatabase,QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import auth
import admin
import income
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel, QSqlQuery
from PyQt5.QtCore import *
import random

class Auth(auth.Auth):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_auth.clicked.connect(self.Enter)
        self.btn_exit.clicked.connect(self.Exit)

    def Enter(self):
        if self.lineEdit.text() == "admin" and self.lineEdit_password.text() == "admin":
            self.admin = Admin()
            self.admin.show()
            self.close()
        else:
            self.test = Captcha()
            self.test.show()

    def Exit(self):
        exe.close()

class Captcha(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(180,150)
        layout = QVBoxLayout()

        self.captcha = QLabel(str(random.randint(1000,9999)))
        self.captcha_edit = QLineEdit()
        self.label = QLabel("Каптча")
        self.captcha_btn = QPushButton("Проверить")
        self.timer_label = QLabel("Таймер: 10")
        self.count = 10
        self.timer_label.setText(str(self.count))
        self.timer = QTimer()

        layout.addWidget(self.label)
        layout.addWidget(self.captcha)
        layout.addWidget(self.captcha_btn)
        layout.addWidget(self.captcha_edit)
        layout.addWidget(self.timer_label)

        self.captcha_btn.clicked.connect(self.captcha_click)
        self.timer.timeout.connect(self.timer_tick)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        with open ('style.css') as style:
            self.setStyleSheet(style.read())

    def captcha_click(self):
        if self.captcha_edit.text() == self.captcha.text():
            QMessageBox.information(self, "Верно", "Верно")
            Captcha.close(self)
        else:
            self.captcha_edit.setDisabled(True)
            self.timer.start()
            QMessageBox.critical(self, "Ошибка", "Ошибка")  

    def timer_tick(self):
        self.timer.start(1000)
        self.count -= 1
        self.timer_label.setText(str(self.count))

        if self.count == 0:
            self.timer.stop()
            self.captcha_edit.setDisabled(False) 

class Admin(admin.Admin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        db = QSqlDatabase.addDatabase('QPSQL')
        db.setDatabaseName('doxod')
        db.setHostName('localhost')
        db.setPort(5432)
        db.setUserName('postgres')
        db.setPassword('student')
        db.open()
        self.db = db
        query = QSqlQueryModel()
        sql = "SELECT * FROM public.company"
        query.setQuery(sql)
        self.tableView.setModel(query)
        self.tableView.setColumnHidden(0, True)
        
        self.pushButton.clicked.connect(self.Income)
        self.pushButton_exit.clicked.connect(self.Exit)
        self.pushButton_2.clicked.connect(self.Form)

    def Income(self):
        self.income = Income(self.db, self.tableView)
        self.income.show()

    def Form(self):
        pass

    def Exit(self):
        self.close()

    
class Income(income.Income):
    def __init__(self, db, tableView):
        super().__init__()
        self.tableView = tableView
        self.db = db
        self.setupUi(self)

        self.pushButton_db.clicked.connect(self.Doxod)
        self.pushButton_exit.clicked.connect(self.Exit)

    def Doxod(self):
        model = QSqlQueryModel()
        # q = QSqlQuery()
        model.setQuery(f"INSERT INTO public.company (organization, income) VALUES ('{self.lineEdit_ip.text()}', '{self.lineEdit_income.text()}')")
        # print(q.isActive())
        model.clear()
        model.setQuery("SELECT * FROM public.company")
        self.tableView.setModel(model)
        self.lineEdit_ip.text()
        self.lineEdit_income.text()

    def Exit(self):
        self.close()

app = QApplication(sys.argv)
exe = Auth()
exe.show()
app.exec()