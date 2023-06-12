from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from MySQLdb import _mysql

class CarDetails(QWidget):
    def __init__(self,db,id):
        super().__init__()
        uic.loadUi('./widgets/gui/mainDisplay.ui', self)
        self.db = db
        self.id = id

        self.editBtn.clicked.connect(self.editCar)
        self.deleteBtn.clicked.connect(self.deleteCar)

        self.updateDisplay()



    def updateDisplay(self):
        query = """
        SELECT * 
        FROM cars
        WHERE id = '%s'
        """ % (''.join(str(self.id)))
        self.db.query(query)
        results = self.db.store_result()
        car = results.fetch_row(1,1)
        dislpay = f"""
        Year: {car[0]["year"].decode('utf-8')}\n
        Make: {car[0]["make"].decode('utf-8')}\n
        Model: {car[0]["model"].decode('utf-8')}\n
        Country: {car[0]["country"].decode('utf-8')}\n
        Price: ${car[0]["price"].decode('utf-8')}
        """
        self.carDetails.setText(dislpay)

    def editCar(self,id):
        print('edit Clicked',self.id)

    def deleteCar(self,id):
        print('delete Clicked',self.id)