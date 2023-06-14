from PyQt6.QtWidgets import QMainWindow, QPushButton
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
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, CarForm(db,self.updateCentralWidget))
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, CarList(db,self.updateCentralWidget))
        self.setCentralWidget(CarDetails(db,4,self.updateCentralWidget,self.updateLeftDock,self.updateRightDock))
        
        self.button = QPushButton("hhh", self)
        self.button.clicked.connect(self.updateCentralWidget)

    def updateCentralWidget(self,id):
        print('update center')
        self.setCentralWidget(CarDetails(self.db,self.updateCentralWidget,id))

    def updateLeftDock(self):
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, CarForm(db,self.updateCentralWidget))

    def updateRightDock(self):
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, CarList(db,self.updateCentralWidget))