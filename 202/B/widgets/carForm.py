from PyQt6.QtWidgets import QDockWidget,QMessageBox
from PyQt6 import uic

class CarForm(QDockWidget):
    def __init__(self,db):
        super().__init__()
        uic.loadUi('./widgets/gui/carForm.ui',self)
        self.db = db
        self.submitBtn.clicked.connect(self.createNewCar)

    def createNewCar(self):
        year = self.inputYear.currentText()
        make = self.inputMake.currentText()
        model = self.inputModel.text()
        country = self.inputCountry.currentText()
        price = self.inputPrice.text()

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
        try:
            self.db.query(query)
            dialog = QMessageBox(parent=self,text="Created Succesfully!")
            dialog.setWindowTitle('App Message')
            ret = dialog.exec()
        except Exception as e:
            dialog = QMessageBox(parent=self,text=f"Creation Failed...\n{e}")
            dialog.setWindowTitle('App Message')
            ret = dialog.exec()


