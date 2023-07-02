import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6 import uic
from MySQLdb import _mysql
from mainWindow import MainWindow

class Login(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./views/userManagement.ui', self)
        self.usernameLabel.setProperty('class', 'label')
        self.usernameInput.setProperty('class', 'input')
        self.passwordLabel.setProperty('class', 'label')
        self.passwordInput.setProperty('class', 'input')
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.submitBtn.clicked.connect(self.checkCredentials)


        self.connect_to_db()

    def connect_to_db(self):
        try:
            self.db = _mysql.connect('localhost','root','root','pyqt_chores')
            print('Database Connection Established...')
        except Exception as e:
            print('Database Connection Failed, Error: ',e)


    def checkCredentials(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        
        query = f"SELECT * FROM users WHERE username = '{username}';"
        self.db.query(query)
        store = self.db.store_result()
        user = store.fetch_row(1,1)
        
        if user:
            if user[0]['password'].decode('utf-8') == password:
                self.mainWindow = MainWindow()
                with open('css/main.css','r') as file:
                    self.mainWindow.setStyleSheet(file.read())
                self.mainWindow.show()
                self.close()
        self.status.setText('Invalid Login')
        self.status.setStyleSheet('color: #700;font-size: 21px;')

if __name__=='__main__':
    app = QApplication(sys.argv)

    main = Login()
    with open('css/form.css','r') as file:
        app.setStyleSheet(file.read())
    main.show()


try:
    sys.exit(app.exec())
except SystemExit:
    print ('Goodbye...')