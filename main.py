import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt5.QtWidgets import QApplication, QMainWindow

from config import ui_file, db_name, query


class CoffeeViewerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)

        self.con = sqlite3.connect("films_db.sqlite")
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(db_name)
        self.db.open()
        self.model = QSqlTableModel()
        self.coffee_table.setModel(self.model)

        self.update_table()

    def update_table(self):
        self.model.setQuery(QSqlQuery(query))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CoffeeViewerWindow()
    w.show()
    sys.exit(app.exec_())
