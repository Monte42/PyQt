from PyQt6.QtWidgets import QWidget, QLineEdit
from PyQt6 import uic
from models.User import User
from controllers.users import UserController
from utils.general import decode_model, create_ui_message_box

class UserManager(QWidget):
    def __init__(self,parent,username=None):
        super().__init__()
        uic.loadUi('views/userManagement.ui', self)
        self.usernameLabel.setProperty('class','label')
        self.usernameInput.setProperty('class','input')
        self.passwordLabel.setProperty('class','label')
        self.passwordInput.setProperty('class','input')
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.user=None
        
        self.submitBtn.clicked.connect(self.on_submit)
        self.parent = parent
        self.db = parent.db
        
        if username:
            self.user = User.fetch_user_by_username(self.db, username)['data']
            self.usernameInput.setText(self.user.username)
            self.passwordInput.setText(self.user.password)


    def on_submit(self):
        if self.user:
            updated_user = {
                'id':self.user.id,
                'username':self.usernameInput.text(),
                'password':self.passwordInput.text()
            }
            UserController.update_user(self.db,updated_user)
            self.parent.close()
            self.close()
        else:
            new_user = {
                'username':self.usernameInput.text(),
                'password':self.passwordInput.text()
            }
            result = UserController.create_new_user(self.db,new_user)
            print(result)
            if result['results']:
                self.message_box = create_ui_message_box(f'{self.usernameInput.text()}, Created Successfully!')
                self.message_box.show()
            else:
                msg = ''
                for err in result['errors']:
                    msg += f'{err}\n'
                self.message_box = create_ui_message_box(msg)
                self.message_box.show()
            self.close()