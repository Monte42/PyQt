import sys
import os
import time
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
# New For DB
import MySQLdb as mdb
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(900,700)
        self.setWindowTitle('Main App')
        label = QLabel('Main App!!', parent=self)

class LoginWimdow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.window_width, self.window_height = 350, 125
        self.setFixedSize(self.window_width, self.window_height)

        layout = QGridLayout()
        self.setLayout(layout)

        labels = {}
        self.lineEdits = {}

        labels['username'] = QLabel('Username')
        labels['password'] = QLabel('Password')

        self.lineEdits['username'] = QLineEdit()
        self.lineEdits['password'] = QLineEdit()
        self.lineEdits['password'].setEchoMode(QLineEdit.EchoMode.Password)# Blocks characters for password field

        # layout.addWidget(a0, row, column, rowSpan, columnSpan)
        layout.addWidget(labels['username'], 0, 0, 1, 1)
        layout.addWidget(self.lineEdits['username'], 0, 1, 1, 3)

        layout.addWidget(labels['password'], 1, 0, 1, 1)
        layout.addWidget(self.lineEdits['password'], 1, 1, 1, 3)

        login_btn = QPushButton('&Login')
        login_btn.clicked.connect(self.checkCredentials)
        layout.addWidget(login_btn, 3, 3, 1, 1)

        self.status = QLabel('')
        self.status.setStyleSheet('font-size:22px; color:red;')
        layout.addWidget(self.status, 4, 0, 1, 3)

        self.connectToDB()
    def connectToDB(self):
        try:
            db = mdb.connect('localhost', 'root', 'root', 'pyqt6')
            print('connected to db...')
        except mdb.Error as e:
            print('no', e)
            sys.exit(1)

    def checkCredentials(self):
        username = self.lineEdits['username'].text()
        password = self.lineEdits['password'].text()

        query = QSqlQuery()
        query.prepare('SELECT * FROM user WHERE username=:username')
        query.bindValue(':username', username)
        query.exec()

        if query.first():
            if query.value('password') == password:
                time(1)
                self.mainApp = MainApp()
                self.mainApp.show()
                self.close()
            else:
                self.status.setText('invalid login')
        else:
            self.status.setText('Invalid Login')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    loginWindow = LoginWimdow()
    loginWindow.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Goodbye...')


