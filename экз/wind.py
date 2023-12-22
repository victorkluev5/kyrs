import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel
from PyQt5.QtCore import *
from auth import Auth
from sklad import Sklad
from capth import Captcha
from tovar import Tovar
from admin import Admin
from people import People

class Auth(Auth):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        db = QSqlDatabase.addDatabase('QPSQL')
        db.setDatabaseName('sklad')
        db.setHostName('localhost')
        db.setPort(5432)
        db.setUserName('postgres')
        db.setPassword('student')
        db.open()
        self.db = db

        self.btn_auth.clicked.connect(self.Enter)
        self.btn_exit.clicked.connect(self.Exit)

    def Enter(self):
        query = QSqlQuery()
        query.exec(f"SELECT * FROM public.login WHERE login = '{self.lineEdit_login.text()}' AND password = '{self.lineEdit_pass.text()}'")
        print(self.lineEdit_login.text(), self.lineEdit_pass.text())
        
        if query.first():
            if query.value(0) == 1:
                self.sw = Sklad(self.db)
                self.sw.show()
                self.close()
            
            elif query.value(0) == 2:
                self.sw = Admin(self.db)
                self.sw.show()
                self.close()

        else:
            QMessageBox.critical(self, "ОШИБКА", "Ошибка")
            self.sw = Captcha()
            self.sw.setupUi(self.sw)
            self.sw.show()

    def Exit(sefl):
        sefl.close()

class Sklad(Sklad):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setupUi(self)
        self.setupUi(self)

        query = QSqlQueryModel()
        sql = "SELECT * FROM public.tovar"
        query.setQuery(sql)
        self.tableView.setModel(query)
        self.tableView.setColumnHidden(0, True)
        
        self.btn_tovar.clicked.connect(self.Tovar)
        self.btn_exit.clicked.connect(self.Exit)
        self.btn_delete.clicked.connect(self.Delete)

    def Tovar(self):
        self.tovar = Tovar(self.db, self.tableView)
        self.tovar.show()

    def Delete(self):
        query = QSqlTableModel()
        query.setTable("tovar")
        query.select()
        selected = self.tableView.selectedIndexes()

        rows = set(index.row() for index in selected)
        rows = list(rows)
        rows.sort()
        first = rows[0]

        query.removeRow(first)
        query.select()

        query = QSqlTableModel()
        query.setTable("tovar")
        query.select()
        self.tableView.setModel(query)


    def Exit(self):
        self.close()

class Tovar(Tovar):
    def __init__(self, db, tableView):
        super().__init__()
        self.tableView = tableView
        self.db = db
        self.setupUi(self)

        self.pushButton_tovar.clicked.connect(self.Doxod)
        self.pushButton_exit.clicked.connect(self.Exit)

    def Doxod(self):
        model = QSqlQueryModel()
        date = f"{str(self.dateEdit.date().day())}.{str(self.dateEdit.date().month())}.{str(self.dateEdit.date().year())}"
        model.setQuery(f"INSERT INTO public.tovar (name, quantity, date_delivery, gorod) VALUES ('{self.lineEdit_name.text()}', '{self.lineEdit_quant.text()}', '{date}', '{self.lineEdit_gorod.text()}')")
        model.clear()
        model.setQuery("SELECT * FROM public.tovar")
        self.tableView.setModel(model)
        self.close()

    def Exit(self):
        self.close()

class Admin(Admin):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setupUi(self)
        self.setupUi(self)

        query = QSqlQueryModel()
        sql = "SELECT * FROM public.job_title"
        query.setQuery(sql)
        self.tableView.setModel(query)
        self.tableView.setColumnHidden(0, True)
        self.tableView.setColumnHidden(4, True)       
        self.btn_people_up.clicked.connect(self.People_up)
        self.btn_exit.clicked.connect(self.Exit)
        self.btn_people_del.clicked.connect(self.Delete)

    def People_up(self):
        self.tovar = People(self.db, self.tableView)
        self.tovar.show()

    def Delete(self):
        query = QSqlTableModel()
        query.setTable("jop_title")
        query.select()
        selected = self.tableView.selectedIndexes()

        rows = set(index.row() for index in selected)
        rows = list(rows)
        rows.sort()
        first = rows[0]

        query.removeRow(first)
        query.select()

        query = QSqlTableModel()
        query.setTable("jop_title")
        query.select()
        self.tableView.setModel(query)


    def Exit(self):
        self.close()

class People(People):
    def __init__(self, db, tableView):
        super().__init__()
        self.tableView = tableView
        self.db = db
        self.setupUi(self)

        self.pushButton_tovar.clicked.connect(self.People)
        self.pushButton_exit.clicked.connect(self.Exit)

    def People(self):
        model = QSqlQueryModel()
        model.setQuery(f"INSERT INTO public.job_title (name, surname, jop) VALUES ('{self.lineEdit_name.text()}', '{self.lineEdit_klad.text()}', '{self.comboBox.currentText()}')")
        model.clear()
        model.setQuery("SELECT * FROM public.job_title")
        self.tableView.setModel(model)
        self.close()

    def Exit(self):
        self.close()


app = QApplication(sys.argv)
exe = Auth()
exe.show()
app.exec()