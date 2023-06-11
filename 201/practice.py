import sys
import os
import time
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
# New For DB
from MySQLdb import _mysql

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

        # Create a func to connent to db, then call that func on init
        self.connectToDB()


    def connectToDB(self):
        try:
            # Call MySql.connect() and store in a class var for later use
            # _mysql.connect(server, username, password, database name)
            self.db = _mysql.connect('localhost', 'root', 'root', 'pyqt6')
            print('Connected to DB...')
        except Exception as e:
            print('Failed to connect to DB',e)
            sys.exit(1)

    def checkCredentials(self):
        username = self.lineEdits['username'].text()
        password = self.lineEdits['password'].text()

        query = """SELECT * FROM users WHERE username = '%s';""" % (''.join(username))
        print(f'Running Query: {query}')
        self.db.query(query)
        
        results = self.db.store_result()
        user = results.fetch_row(1,1)


        if user:
            if user[0]['password'].decode('utf-8') == password:
                self.mainApp = MainApp()
                self.mainApp.show()
                self.close()
        self.status.setText('Invalid Login')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    loginWindow = LoginWimdow()
    loginWindow.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Goodbye...')


