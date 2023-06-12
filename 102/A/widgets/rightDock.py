from PyQt6.QtWidgets import QDockWidget, QTableWidgetItem
from PyQt6 import uic
from MySQLdb import _mysql

class RightDock(QDockWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./gui/rightDock.ui', self)
