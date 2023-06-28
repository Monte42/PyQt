from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from PyQt6 import uic
from widgets.calculator import Calculator
from widgets.adminDashboard import AdminDashboard

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./views/main.ui', self)

        self.openCalculator(True)



        self.enterAdmin.triggered.connect(self.openAdminDashboard)
        self.showCalculator.triggered.connect(self.openCalculator)

    def openCalculator(self,firstOpen=False):
        if not firstOpen: self.removeDockWidget(self.layout().itemAt(0).widget())
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, Calculator())
        with open('css/calculator.css','r') as file:
            for i in range(self.layout().count()):
                print(self.layout().itemAt(i).widget())
            self.layout().itemAt(0).widget().setStyleSheet(file.read())
        print('\n\n\n')

    def openAdminDashboard(self):
        self.adminDashboard = AdminDashboard()
        self.adminDashboard.show()