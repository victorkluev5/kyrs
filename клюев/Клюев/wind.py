import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtSql import QSqlDatabase,QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QApplication, QWidget, QTableView
import auth
import admin
import income
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel, QSqlQuery
from PyQt5.QtCore import *


class Auth(auth.Auth):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_auth.clicked.connect(self.Enter)
        self.btn_exit.clicked.connect(self.Exit)

    def Enter(self):
        if self.lineEdit.text() == "1" and self.lineEdit_password.text() == "1":
            self.admin = Admin()
            self.admin.show()
            self.close()
        else:
            self.close()

    def Exit(self):
        exe.close()

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
        self.pushButton_dell.clicked.connect(self.Dell)

    def Income(self):
        self.income = Income(self.db, self.tableView)
        self.income.show()

    def Dell(self):
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
        model.setQuery( f"INSERT INTO public.company (organization, income) VALUES ('{self.lineEdit_ip.text()}', '{self.lineEdit_income.text()}')")
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