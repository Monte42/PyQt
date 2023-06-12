from PyQt6.QtWidgets import QDockWidget
from PyQt6.QtCore import QDate
from PyQt6 import uic

class LeftDock(QDockWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./gui/leftDock.ui', self)
        
        self.updateFunLevel()
        self.inputDate.setDate(QDate(2022, 4, 21))
        
        self.inputFun.valueChanged.connect(self.updateFunLevel)
        self.submitBtn.clicked.connect(self.createNewLocation)
        
    def updateFunLevel(self):
        self.progressBar.setValue(self.inputFun.value())
    
    def createNewLocation(self):
        name = self.inputName.text()
        state = self.inputState.text()
        date = self.inputDate.date().toPyDate().strftime("%m/%d/%Y")
        funLevel = str(self.inputFun.value())

        self.displayData.setText(f'Name:{name}\nState:{state}\nDate:{date}\nFun:{funLevel}\n')