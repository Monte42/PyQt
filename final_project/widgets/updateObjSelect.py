from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from models.User import User
from widgets.userManager import UserManager
from utils.general import create_ui_message_box

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
        result = User.delete_user(self.db,self.objInput.currentText())
        print(result['status'])
        if result['status']:
            self.message_box = create_ui_message_box(f'{result["data"]["username"]} has been successfully deleted...')
            self.message_box.show()
            self.close()
        else:
            msg = ''
            for err in result['errors']:
                msg += f'{err}\n'
            self.message_box = create_ui_message_box(msg)
            self.message_box.show()