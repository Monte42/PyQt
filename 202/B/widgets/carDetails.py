from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QMessageBox
from PyQt6 import uic
from MySQLdb import _mysql
from widgets.carForm import CarForm

class CarDetails(QWidget):
    def __init__(self,db,id,updtCntr,updateRightDock=None):
        super().__init__()
        uic.loadUi('./widgets/gui/mainDisplay.ui', self)
        self.db = db
        self.id = id
        self.updateRtDock = updateRightDock
        self.updateCentralWidget = updtCntr
        self.editBtn.clicked.connect(self.editCar)
        self.deleteBtn.clicked.connect(self.deleteCar)
        self.updateDisplay(self.id)

    def updateDisplay(self,id):
        query = """
        SELECT * 
        FROM cars
        WHERE id = '%s'
        """ % (''.join(str(id)))
        self.db.query(query)
        results = self.db.store_result()
        car = results.fetch_row(0,1)
        dislpay = f"""
        Year: {car[0]["year"].decode('utf-8')}\n
        Make: {car[0]["make"].decode('utf-8')}\n
        Model: {car[0]["model"].decode('utf-8')}\n
        Country: {car[0]["country"].decode('utf-8')}\n
        Price: ${car[0]["price"].decode('utf-8')}
        """
        self.carDetails.setText(dislpay)

    def editCar(self,id):
        dialog = QMainWindow()
        form = CarForm(self.db,self.updateCentralWidget,self.id,self.updateRtDock)
        dialog.setCentralWidget(form)
        dialog.setWindowTitle('Edit Car')
        self.dialog = dialog
        self.dialog.show()

    def deleteCar(self):
        query = f"DELETE FROM cars WHERE id={self.id};"
        try:
            self.db.query(query)
            dialog = QMessageBox(parent=self,text="Delete Succesfully!")
            dialog.setWindowTitle('App Message')
            ret = dialog.exec()
            self.updateCentralWidget(4)
        except Exception as e:
            dialog = QMessageBox(parent=self,text=f"Delete Failed...\n{e}")
            dialog.setWindowTitle('App Message')
            ret = dialog.exec()