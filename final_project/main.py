import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton
from PyQt6 import uic
from MySQLdb import _mysql
from mainWindow import MainWindow
from widgets.userManager import UserManager
from controllers.users import UserController
from utils.general import create_ui_message_box

class Login(QWidget):
    def __init__(self):
        super().__init__()
        # Load UI
        uic.loadUi('./views/userManagement.ui', self)
        # Set Class Property for styling
        self.usernameLabel.setProperty('class', 'label')
        self.usernameInput.setProperty('class', 'input')
        self.passwordLabel.setProperty('class', 'label')
        self.passwordInput.setProperty('class', 'input')
        # Turnd input into redacted display
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)

        # Set up clicked/triggered listeners 
        self.submitBtn.clicked.connect(self.checkCredentials)

        # Run Required opening methods
        self.connect_to_db()

        # Check to see if there are any users
        self.check_existing_users_and_set_submit_btn()


    # Widget Specit Methods
    def connect_to_db(self):
        try:
            self.db = _mysql.connect('localhost','root','root','pyqt_chores')
            print('Database Connection Established...')
        except Exception as e:
            print('Database Connection Failed, Error: ',e)

    def check_existing_users_and_set_submit_btn(self):
        query = 'SELECT * FROM users LIMIT 1;'
        self.db.query(query)
        store = self.db.store_result()
        user = store.fetch_row(1,1)

        if user:
            self.submitBtn.clicked.connect(self.checkCredentials)
        else:
            self.mainHeader.setText('Create Admin User')
            self.submitBtn.clicked.connect(self.create_first_user)

    def checkCredentials(self): # *** <= This cant be in controller due to circular imports
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        
        query = f"SELECT * FROM users WHERE username = '{username}';"
        self.db.query(query)
        store = self.db.store_result()
        user = store.fetch_row(1,1)
        
        if user:
            if user[0]['password'].decode('utf-8') == password:
                self.open_main_window(user[0])
        self.status.setText('Invalid Login')
        self.status.setStyleSheet('color: #700;font-size: 21px;')

    def create_first_user(self):
        new_user = {
            'username': self.usernameInput.text(),
            'password': self.passwordInput.text(),
            'is_admin': True
        }
        data = UserController.create_new_user(self.db,new_user)
        if data['status']:
            user = UserController.get_user_by_username(self.db,new_user['username'])
            self.open_main_window(user['data'])
        else:
            msg = ''
            for err in data['errors']:
                msg += f'{err}\n'
            self.message_box = create_ui_message_box(msg)
            self.message_box.show()

    def open_main_window(self,user):
        self.mainWindow = MainWindow(self.db, user)
        with open('css/main.css','r') as file:
            self.mainWindow.setStyleSheet(file.read())
        self.mainWindow.show()
        self.close()



if __name__=='__main__':
    app = QApplication(sys.argv)

    main = Login()

    with open('css/form.css','r') as file:
        app.setStyleSheet(file.read())
    main.show()


try:
    sys.exit(app.exec())
except SystemExit:
    print ('Goodbye...')