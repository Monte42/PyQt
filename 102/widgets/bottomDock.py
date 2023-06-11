from PyQt6.QtWidgets import QDockWidget
from PyQt6 import uic
from MySQLdb import _mysql

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
        db = _mysql.connect('localhost','root','root','pyqt6')
        query = """
        INSERT INTO cars(year,make,model,country,price)
        VALUES('%s','%s','%s','%s','%s');
        """ % (
            ''.join(year),
            ''.join(make),
            ''.join(model),
            ''.join(country),
            ''.join(price)
        )
        db.query(query)
        self.displayData.setText(f'Ran Query:\n\n{query}')