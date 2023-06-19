import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QListWidgetItem,QMessageBox
from PyQt6.QtCore import Qt
from PyQt6 import uic
from MySQLdb import _mysql
from models.Car import Car

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('views/main.ui', self)

        # Buttons
        self.listAllCars.itemClicked.connect(self.on_item_click)
        self.createBtn.clicked.connect(self.create_new_car)
        self.deleteBtn.clicked.connect(self.delete_car)
        self.editBtn.clicked.connect(self.open_edit_window)

        # Connect to DB
        self.connect_to_db()

        # Populate App with data
        self.populate_car_list()
        self.populate_car_details()

    # ===========
    # APP METHODS
    # ===========

    def connect_to_db(self):
        try:
            self.db = _mysql.connect('localhost','root','root','pyqt6')
            print('Connected to DB..')
        except Exception as e:
            print(f'****\nConnection Failed...\n****\n\n',e)

    def on_item_click(self,item):
        id = item.text().split('|')[1]
        self.populate_car_details(id)

    def open_edit_window(self):
        editWindow = QMainWindow()
        form = uic.loadUi('views/update.ui')
        form.inputYear.setText(self.current_car.year)
        form.inputMake.setText(self.current_car.make)
        form.inputModel.setText(self.current_car.model)
        form.inputCountry.setText(self.current_car.country)
        form.inputPrice.setText(self.current_car.price)
        form.updateBtn.clicked.connect(self.update_car)
        editWindow.setWindowTitle(f'Edit {self.current_car.year} {self.current_car.model}')
        editWindow.setCentralWidget(form)
        self.editWindow = editWindow
        self.editWindow.show()


    # CREATE
    # =======
    def create_new_car(self):
        new_car = {
            'year': int(self.inputYear.text()),
            'make': self.inputMake.text(),
            'model': self.inputModel.text(),
            'country': self.inputCountry.text(),
            'price': int(self.inputPrice.text())
        }
        Car.create_car(self.db,new_car)
        self.populate_car_list()
        self.populate_car_details()
        self.inputYear.setText('')
        self.inputMake.setText('')
        self.inputModel.setText('')
        self.inputCountry.setText('')
        self.inputPrice.setText('')


    # READ
    # =====
    def populate_car_list(self):
        self.listAllCars.clear()
        self.all_cars = Car.get_all_cars(self.db)
        for car in self.all_cars:
            QListWidgetItem(self.all_cars[car].display_list_data(), self.listAllCars)

    def populate_car_details(self,id=None):
        if id:
            this_car = Car.get_car_by_id(self.db,id)
            self.carDisplay.setText(this_car.display_full_data())
            self.current_car = this_car
        else:
            lastest_car = self.all_cars[len(self.all_cars)-1]
            this_car = Car.get_car_by_id(self.db,lastest_car.get_id())
            self.carDisplay.setText(this_car.display_full_data())
            self.current_car = this_car



    # UPDATE
    # =======
    def update_car(self):
        form = self.editWindow.children()[1]
        updated_car = {
            'id': int(self.current_car.id),
            'year': int(form.inputYear.text()),
            'make': form.inputMake.text(),
            'model': form.inputModel.text(),
            'country': form.inputCountry.text(),
            'price': int(form.inputPrice.text())
        }
        results = Car.update_car(self.db,updated_car)
        if results[0]:
            self.populate_car_list()
            self.populate_car_details(results[1])
            dialog = QMessageBox(parent=self,text=f"Successfully Updated ID: {results[1]}")
            dialog.setWindowTitle('App Message')
            ret = dialog.exec()
            self.editWindow.close()
        else:
            dialog = QMessageBox(parent=self,text=f"Update Failed...\n{results[1]}")
            dialog.setWindowTitle('App Message')
            ret = dialog.exec()


    # DELETE
    # =======
    def delete_car(self):
        results = Car.delete_car(self.db, self.current_car.id)
        if results[0]:
            self.populate_car_list()
            self.populate_car_details()
            dialog = QMessageBox(parent=self,text=f"Successfully Deleted ID: {results[1]}")
            dialog.setWindowTitle('App Message')
            ret = dialog.exec()
        else:
            dialog = QMessageBox(parent=self,text=f"Delete Failed...\n{results[1]}")
            dialog.setWindowTitle('App Message')
            ret = dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = MainWindow()
    main.show()

try: sys.exit(app.exec())
except: print('Goodbye...')