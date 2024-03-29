from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6 import uic
from widgets.calculator import Calculator
from widgets.adminDashboard import AdminDashboard
from utils import general

class MainWindow(QMainWindow):
    def __init__(self,db,user):
        super().__init__()
        # Loading the UI
        uic.loadUi('./views/main.ui', self)
        self.current_user = general.decode_model(user) #Storing logged in user & decode
        self.appTitle.setText(f"Welcome, {self.current_user['username']}")
        self.db = db
        # Set up clicked/triggered listeners
        self.enterAdmin.triggered.connect(self.openAdminDashboard)
        self.showCalculator.triggered.connect(self.openCalculator)

        # Run Required opening methods
        self.openCalculator(True)



    # Widget Specit Methods
    def openCalculator(self,firstOpen=False):
        if not firstOpen: self.removeDockWidget(self.layout().itemAt(0).widget())
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, Calculator())
        with open('css/calculator.css','r') as file:
            self.layout().itemAt(0).widget().setStyleSheet(file.read())

    def openAdminDashboard(self):
        if self.current_user['is_admin']:
            self.adminDashboard = AdminDashboard(self.db)
            with open('css/adminDashboard.css','r') as file:
                self.adminDashboard.setStyleSheet(file.read())
            self.adminDashboard.show()
        else:
            self.messageBox = general.create_ui_message_box('You Are Not An Authorized User!')
            self.messageBox.show()