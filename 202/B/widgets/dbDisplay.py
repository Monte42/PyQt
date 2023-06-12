from PyQt6.QtWidgets import QDockWidget,QListWidgetItem
from PyQt6 import uic

class CarList(QDockWidget):
    def __init__(self,db):
        super().__init__()
        uic.loadUi('./widgets/gui/carList.ui', self)
        self.db = db
        self.updateBtn.clicked.connect(self.getAllCars)
        self.carList.itemClicked.connect(self.carDetails)
        self.getAllCars()

    def getAllCars(self):
        self.carList.clear()
        query = """SELECT * FROM cars;"""
        self.db.query(query)
        results = self.db.store_result()
        all_cars = results.fetch_row(0,1)
        for car in all_cars:
            li = QListWidgetItem(f"{car['id'].decode('utf-8')} {car['year'].decode('utf-8')} {car['model'].decode('utf-8')}", self.carList)

    def carDetails(self,item):
        print('Hello',item.text()[0])