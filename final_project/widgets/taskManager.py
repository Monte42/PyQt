from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

class TaskManager(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('views/taskManagement.ui', self)