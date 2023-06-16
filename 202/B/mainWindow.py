from PyQt6.QtWidgets import QMainWindow, QPushButton, QHBoxLayout,QWidget
from PyQt6.QtCore import Qt
from PyQt6 import uic

from widgets.carForm import CarForm
from widgets.dbDisplay import CarList
from widgets.carDetails import CarDetails


class MainWindow(QMainWindow):
    def __init__(self,db):
        super().__init__()
        uic.loadUi('./widgets/gui/mainWindow.ui', self)
        self.db = db
        self.updateCentralWidget(4)

    def updateCentralWidget(self,id):
        layout = QHBoxLayout()
        layout.addWidget(CarForm(self.db,self.updateCentralWidget))
        layout.addWidget(CarList(self.db,self.updateCentralWidget))
        layout.addWidget(CarDetails(self.db,id,self.updateCentralWidget))
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)