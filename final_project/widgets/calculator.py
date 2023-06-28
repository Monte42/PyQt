from PyQt6.QtWidgets import QDockWidget
from PyQt6 import uic

class Calculator(QDockWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('views/calc.ui', self)

        self.btn_1.setProperty('class','action-btn')