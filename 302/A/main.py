import sys
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtCore import Qt
from PyQt6 import uic
from MySQLdb import _mysql

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('views/main.ui', self)







        self.connect_to_db()
    def connect_to_db(self):
        try:
            self.db = _mysql.connect('localhost','ro6t','root','pyqt_books')
            print('Beep Boop, DB is up...')
        except Exception as e:
            print('Bop Boop Beep, something went wrong. so very wrong...')









if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = MainWindow()
    main.show()

try: sys.exit(app.exec())
except: print('Goodbye Bop Boop Bing...')