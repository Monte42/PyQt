from PyQt6.QtWidgets import QDockWidget
from PyQt6 import uic

class CarList(QDockWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./widgets/gui/carList.ui', self)