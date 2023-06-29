from PyQt6.QtWidgets import QWidget, QLineEdit
from PyQt6 import uic

class UserManager(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('views/userManagement.ui', self)

        self.usernameLabel.setProperty('class','label')
        self.usernameInput.setProperty('class','input')
        self.passwordLabel.setProperty('class','label')
        self.passwordInput.setProperty('class','input')
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
