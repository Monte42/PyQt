from PyQt6.QtWidgets import QDockWidget
from PyQt6.QtCore import QDate
from PyQt6 import uic
from MySQLdb import _mysql

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
        db = _mysql.connect('localhost','root','root','pyqt6')
        query = """
        INSERT INTO locations(name,state,visit_date,fun_level)
        VALUES('%s','%s','%s','%s');
        """ % (''.join(name),''.join(state),''.join(date),''.join(funLevel))
        db.query(query)
        self.displayData.setText(f'Name:{name}\nState:{state}\nDate:{date}\nFun:{funLevel}\nCREATED...')