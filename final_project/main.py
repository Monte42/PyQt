import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6 import uic
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


    def checkCredentials(self):
        self.mainWindow = MainWindow()
        with open('css/main.css','r') as file:
            self.mainWindow.setStyleSheet(file.read())
        self.mainWindow.show()
        self.close()

if __name__=='__main__':
    app = QApplication(sys.argv)

    main = Login()
    with open('css/userManagement.css','r') as file:
        app.setStyleSheet(file.read())
    main.show()


try:
    sys.exit(app.exec())
except SystemExit:
    print ('Goodbye...')