from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from PyQt6 import uic
from widgets.calculator import Calculator
from widgets.adminDashboard import AdminDashboard

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./views/main.ui', self)

        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, Calculator())
        with open('css/calculator.css','r') as file:
            self.layout().itemAt(0).widget().setStyleSheet(file.read())



        self.enterAdmin.triggered.connect(self.openAdminDashboard)

    def openAdminDashboard(self):
        self.adminDashboard = AdminDashboard()
        self.adminDashboard.show()