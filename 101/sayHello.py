import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6 import uic

class SayHelloWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUIs/sayHelloWidget.ui',self)
        self.btn.clicked.connect(self.sayHello)



    def sayHello(self):
        inputTxt = self.input.text()
        self.output.setText(f'Hello There {inputTxt}')



if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = SayHelloWidget()
    widget.show()

try:
    sys.exit(app.exec())
except SystemExit:
    print('Goodbye...')