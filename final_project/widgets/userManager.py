from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

class UserManager(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('views/userManagement.ui', self)