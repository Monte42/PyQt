from PyQt6.QtWidgets import QDockWidget
from PyQt6 import uic

class CarForm(QDockWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./widgets/gui/carForm.ui',self)