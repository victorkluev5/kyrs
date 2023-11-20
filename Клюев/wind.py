import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QApplication, QMessageBox
import auth
import admin
import income
import user
# import random
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel
from PyQt5.QtCore import *
from capth import Captcha

class Auth(auth.Auth):
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

        self.btn_auth.clicked.connect(self.Enter)
        self.btn_exit.clicked.connect(self.Exit)

        

    def Enter(self):
        # if self.lineEdit.text() == "admin" and self.lineEdit_password.text() == "admin":
        #     self.admin = Admin()
        #     self.admin.show()
        #     self.close()
        query = QSqlQuery()
        query.exec(f"SELECT * FROM public.profile WHERE login = '{self.lineEdit.text()}' AND password = '{self.lineEdit_password.text()}'")
        print(self.lineEdit.text(), self.lineEdit_password.text())
        
        if query.first():
            if query.value(3) == 1:
                self.sw = Admin()
                self.sw.show()
                self.close()
            
            elif query.value(3) == 2:
                self.sw = User()
                self.sw.show()
                self.close()

        else:
            QMessageBox.critical(self, "ОШИБКА", "Ошибка")
            self.sw = Captcha()
            self.sw.setupUi(self.sw)
            self.sw.show()

    def Exit(self):
        self.close()

class User(user.User):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        query = QSqlQueryModel()
        sql = "SELECT * FROM public.company"
        query.setQuery(sql)
        self.tableView.setModel(query)
        self.tableView.setColumnHidden(0, True)

        self.pushButton_exit1.clicked.connect(self.Exit1)

    def Exit1(self):
        self.close()

# class Captcha1(Captcha):
#     def __init__(self):
#         super().__init__()
        
    
#         # self.setupUi(self)
#         self.setWindowFlags(Qt.FramelessWindowHint)
#         self.label_Kapcha.setText(str(random.randint(1000,9000)))
        
#         self.timer = QTimer()
#         self.count = 10
#         self.label_Time.setText(str(self.count))
#         self.timer.timeout.connect(self.Timer_tick)
        
#         self.pushButton_1.clicked.connect(self.Capath)
        
    
#     def Capath (self):
#         if self.lineEdit_kapcha.text() == self.label_Kapcha.text():
#             QMessageBox.information(self, "Успех", "Капча введена правильно")
#             self.close()
#         else:
#             self.lineEdit_kapcha.setDisabled(True)
#             self.timer.start()
#             QMessageBox.critical(self, "ОШИБКА", "Вы ввели неправильно")
#             self.Timer_tick()
            
#     def Timer_tick(self):
#         self.timer.start(1000)
#         self.count -=1
#         self.label_Time.setText(str(self.count))
        
#         if  self.count == 0:
#             self.timer.stop()
#             self.count =10
#             self.lineEdit_kapcha.setDisabled(False)

class Admin(admin.Admin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        query = QSqlQueryModel()
        sql = "SELECT * FROM public.company"
        query.setQuery(sql)
        self.tableView.setModel(query)
        self.tableView.setColumnHidden(0, True)
        
        self.pushButton.clicked.connect(self.Income)
        self.pushButton_exit.clicked.connect(self.Exit)
        self.pushButton_del.clicked.connect(self.Delete)
        self.pushButton_2.clicked.connect(self.Form)

    def Income(self):
        self.income = Income(self.db, self.tableView)
        self.income.show()

    def Delete(self):
        query = QSqlTableModel()
        query.setTable("company")
        query.select()
        selected = self.tableView.selectedIndexes()

        rows = set(index.row() for index in selected)
        rows = list(rows)
        rows.sort()
        first = rows[0]

        query.removeRow(first)
        query.select()

        query = QSqlTableModel()
        query.setTable("company")
        query.select()
        self.tableView.setModel(query)

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
        date = f"{str(self.dateEdit.date().day())}.{str(self.dateEdit.date().month())}.{str(self.dateEdit.date().year())}"
        model.setQuery(f"INSERT INTO public.company (organization, income, data) VALUES ('{self.lineEdit_ip.text()}', '{self.lineEdit_income.text()}', '{date}')")
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