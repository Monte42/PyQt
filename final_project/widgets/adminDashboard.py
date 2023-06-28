from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from widgets.choreManager import ChoreManager
from widgets.taskManager import TaskManager
from widgets.userManager import UserManager

class AdminDashboard(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('views/adminDashboard.ui', self)


        self.newChoreBtn.clicked.connect(self.openNewChoreForm)
        self.newTaskBtn.clicked.connect(self.openNewTaskForm)
        self.newUserBtn.clicked.connect(self.openNewUserForm)




    def openNewChoreForm(self):
        self.choreForm = ChoreManager()
        with open('css/form.css','r') as file:
            self.choreForm.setStyleSheet(file.read())
        self.choreForm.show()
    def openNewTaskForm(self):
        self.taskForm = TaskManager()
        with open('css/form.css','r') as file:
            self.taskForm.setStyleSheet(file.read())
        self.taskForm.show()
    def openNewUserForm(self):
        self.userForm = UserManager()
        with open('css/form.css','r') as file:
            self.userForm.setStyleSheet(file.read())
        self.userForm.show()