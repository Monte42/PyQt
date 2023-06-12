from PyQt6.QtWidgets import QDockWidget
from PyQt6 import uic

class BottomDock(QDockWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./gui/bottomDock.ui',self)
        
        self.submitBtn.clicked.connect(self.createNewCar)
        
        
    def createNewCar(self):
        year = self.inputYear.currentText()
        make = self.inputMake.currentText()
        model = self.inputModel.text()
        country = self.inputCountry.currentText()
        price = self.inputPrice.text()

        display = f"""
        Year: {year}\n
        Year: {make}\n
        Year: {model}\n
        Year: {country}\n
        Year: ${price}\n
        """ 

        self.displayData.setText(display)