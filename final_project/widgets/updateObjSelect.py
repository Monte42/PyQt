from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from models.User import User
from widgets.userManager import UserManager

class UpdateObjSelect(QWidget):
    def __init__(self,db):
        super().__init__()
        uic.loadUi('views/updateObjSelect.ui', self)
        self.objInput.setProperty('class','input')
        self.db = db

        self.submitBtn.clicked.connect(self.openEditUserForm)
        self.deleteBtn.clicked.connect(self.deleteUser)


    def openEditUserForm(self):
        self.userForm = UserManager(self, self.objInput.currentText())
        with open('css/form.css','r') as file:
            self.userForm.setStyleSheet(file.read())
        self.userForm.show()

    def deleteUser(self):
        User.delete_user(self.db,self.objInput.currentText())
        self.close()