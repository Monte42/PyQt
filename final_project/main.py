import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6 import uic
from mainWindow import MainWindow

class Login(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./views/userManagement.ui', self)

        self.submitBtn.clicked.connect(self.checkCredentials)


    def checkCredentials(self):
        self.mainWindow = MainWindow()
        self.mainWindow.show()
        self.close()

if __name__=='__main__':
    app = QApplication(sys.argv)

    main = Login()
    main.show()


try:
    sys.exit(app.exec())
except SystemExit:
    print ('Goodbye...')