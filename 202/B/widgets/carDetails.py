from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

class CarDetails(QWidget):
    def __init__(self,id):
        super().__init__()
        uic.loadUi('./widgets/gui/mainDisplay.ui', self)
        self.carDetails.setText(f'Year:UNK\nMake:UNK\nModel:UNK\nCountry:UNK\nPrice:UNK')
