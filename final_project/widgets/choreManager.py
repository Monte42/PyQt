from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class ChoreManager(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('views/choreManager.ui', self)
