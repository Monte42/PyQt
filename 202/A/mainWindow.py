from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from PyQt6 import uic

from widgets.carForm import CarForm
from widgets.dbDisplay import CarList


class MainWindow(QMainWindow):
    def __init__(self,db):
        super().__init__()
        uic.loadUi('./widgets/gui/mainWindow.ui', self)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, CarForm())
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, CarList())