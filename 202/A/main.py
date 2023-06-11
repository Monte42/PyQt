import sys
# Import PyQt6
from PyQt6.QtWidgets import QWidget,QApplication,QGridLayout,QLabel,QLineEdit,QPushButton
from PyQt6.QtCore import Qt
# For Connecting to DB
from MySQLdb import _mysql

# Import Main Window
from mainWindow import MainWindow

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setFixedSize(350,125)

        # Apply Grid Layout
        layout = QGridLayout()
        self.setLayout(layout)

        # Create Widget Containers
        labels ={}
        self.inputs = {}

        # Lable Wdigets
        labels['username'] = QLabel('Username')
        labels['password'] = QLabel('Password')

        # Input Widgets
        self.inputs['username'] = QLineEdit()
        self.inputs['password'] = QLineEdit()
            # Remember setEchoMode can be used to hide input
        self.inputs['password'].setEchoMode(QLineEdit.EchoMode.Password)

        # Add Widgets to layout
        layout.addWidget(labels['username'], 0, 0, 1, 1)
        layout.addWidget(self.inputs['username'], 0, 1, 1, 3)
        layout.addWidget(labels['password'], 1, 0, 1, 1)
        layout.addWidget(self.inputs['password'], 1, 1, 1, 3)
        loginBtn = QPushButton('&Login')
        loginBtn.clicked.connect(self.checkCredentials)
        layout.addWidget(loginBtn, 3, 3, 1, 1)
        self.status = QLabel('')
        self.status.setStyleSheet('font-size:22px; color:red;')
        layout.addWidget(self.status, 4, 0, 1, 3)

        # Connect to DB
        self.connectToDB()



    # Class Methods
    def connectToDB(self):
        try:
            self.db = _mysql.connect('localhost', 'root', 'root', 'pyqt6')
            print('Connected to DB...')
        except Exception as e:
            print(f'*****\nConnection Failed...\n*****\n\n', e)
            sys.exit(1)

    def checkCredentials(self):
        username = self.inputs['username'].text()
        password = self.inputs['password'].text()

        query = """SELECT * FROM users WHERE username = '%s';""" % (''.join(username))
        self.db.query(query)

        results = self.db.store_result()
        user = results.fetch_row(1,1)

        if user:
            if user[0]['password'].decode('utf-8') == password:
                self.maninWindow = MainWindow(self.db)
                self.maninWindow.show()
                self.close()
        self.status.setText('Invalid Login')




if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Main()
    main.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Goodbye...')