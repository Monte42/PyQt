from PyQt6.QtWidgets import QWidget,QListWidgetItem
from PyQt6 import uic


class CarList(QWidget):
    # When I want to update the car details display I have to do that
    #   from the mainWindow.  To achieve this I created a function in
    #   the MainWindow class (see mainWindow.py) and passed it to this
    #   class        Right Here  VVVVVVVV
    def __init__(self,db,updateCentralWidget):
        super().__init__()
        uic.loadUi('./widgets/gui/carList(2).ui', self)
        self.db = db
        self.updateBtn.clicked.connect(self.getAllCars)
        self.carList.itemClicked.connect(self.carDetails)
        self.getAllCars()
        #  I then gave a place in this class
        self.updateCarDetails = updateCentralWidget

    def getAllCars(self):
        self.carList.clear()
        query = """SELECT * FROM cars;"""
        self.db.query(query)
        results = self.db.store_result()
        all_cars = results.fetch_row(0,1)
        for car in all_cars:
            li = QListWidgetItem(f"{car['id'].decode('utf-8')}|{car['year'].decode('utf-8')} {car['model'].decode('utf-8')}", self.carList)

    def carDetails(self,item):
        id = item.text().split('|')[0]
        # Now I was able to call it from the mainWindow file to update it here 
        self.updateCarDetails(id)