from PyQt6.QtWidgets import QDockWidget,QMessageBox
from PyQt6 import uic
from widgets.dbDisplay import CarList

class CarForm(QDockWidget):
    def __init__(self,db,updtCntr,id=None,updateLeftDock=None,updateRightDock=None):
        super().__init__()
        uic.loadUi('./widgets/gui/carForm.ui',self)
        self.db = db
        self.updateCentralWidget = updtCntr
        self.updateLeftDock = updateLeftDock
        self.updateRightDock = updateRightDock
        self.submitBtn.clicked.connect(self.onSubmit)
        
        if id:
            self.id = id
            self.populateForm()

    def createNewCar(self):
        # reset form back to blank
        # update car list
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
        

    def updateCar(self):
        # close edit form
        # update car detals and list 
        query = f"""
        UPDATE cars
        SET year={self.inputYear.currentText()},
        make='{self.inputMake.currentText()}',
        model='{self.inputModel.text()}',
        country='{self.inputCountry.currentText()}',
        price={self.inputPrice.text()}
        WHERE id = {self.id};
        """
        print(query)
        try:
            self.db.query(query)
            dialog = QMessageBox(parent=self,text="Update Succesfully!")
            dialog.setWindowTitle('App Message')
            ret = dialog.exec()
            self.updateCentralWidget(self.id)
            CarList(self.db,self.updateCentralWidget).getAllCars()
        except Exception as e:
            dialog = QMessageBox(parent=self,text=f"Update Failed...\n{e}")
            dialog.setWindowTitle('App Message')
            ret = dialog.exec()

    def onSubmit(self):
        self.updateCar() if id else self.createNewCar()
        self.parent().close()
        


    def populateForm(self):
        query = """
        SELECT * FROM cars
        WHERE id = '%s';
        """ % (''.join(str(self.id)))
        self.db.query(query)
        results = self.db.store_result()
        car = results.fetch_row(1,1)
        self.inputYear.setCurrentText(car[0]['year'].decode('utf-8'))
        self.inputMake.setCurrentText(car[0]['make'].decode('utf-8'))
        self.inputModel.setText(car[0]['model'].decode('utf-8'))
        self.inputCountry.setCurrentText(car[0]['country'].decode('utf-8'))
        self.inputPrice.setText(car[0]['price'].decode('utf-8'))

