from PyQt6.QtWidgets import QDockWidget
from PyQt6 import uic

class RightDock(QDockWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./gui/rightDock.ui', self)