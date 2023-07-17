from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from controllers.users import UserController 
from widgets.choreManager import ChoreManager
from widgets.userManager import UserManager
from widgets.taskManager import TaskManager
from widgets.updateObjSelect import UpdateObjSelect
from utils.general import decode_model

class AdminDashboard(QWidget):
    def __init__(self,db):
        super().__init__()
        uic.loadUi('views/adminDashboard.ui', self)
        self.db = db

        self.newTaskBtn.clicked.connect(self.openNewTaskForm)
        self.newUserBtn.clicked.connect(self.openNewUserForm)

        self.editTaskBtn.clicked.connect(self.openEditTaskForm)
        self.editUserBtn.clicked.connect(self.openEditUserForm)

        self.choreManagerBtn.clicked.connect(self.openChoreManager)




    def openNewTaskForm(self):
        self.taskForm = TaskManager()
        with open('css/form.css','r') as file:
            self.taskForm.setStyleSheet(file.read())
        self.taskForm.show()

    def openNewUserForm(self):
        self.userForm = UserManager(self)
        with open('css/form.css','r') as file:
            self.userForm.setStyleSheet(file.read())
        self.userForm.show()



    def openEditTaskForm(self):
        self.taskForm = TaskManager()
        with open('css/form.css','r') as file:
            self.taskForm.setStyleSheet(file.read())
        self.taskForm.show()

    def openEditUserForm(self):
        self.objSelect = UpdateObjSelect(self.db)
        all_usernames = UserController.get_all_users(self.db)
        for user in all_usernames:
            self.objSelect.objInput.addItem(user['username'].decode('utf-8'))
        with open('css/form.css','r') as file:
            self.objSelect.setStyleSheet(file.read())
        self.objSelect.show()



    def openChoreManager(self):
        self.choreForm = ChoreManager()
        with open('css/form.css','r') as file:
            self.choreForm.setStyleSheet(file.read())
        self.choreForm.show()