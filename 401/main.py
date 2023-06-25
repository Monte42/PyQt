import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QHBoxLayout,QLabel
from PyQt6 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)



if __name__ == '__main__':
    app = QApplication(sys.argv)


    main = MainWindow()
    main.show()

try:
    sys.exit(app.exec())
except:
    print('Goodbye...')