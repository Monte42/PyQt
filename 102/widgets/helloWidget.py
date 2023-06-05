from PyQt6.QtWidgets import QWidget, QScrollArea
from PyQt6 import uic

class HelloWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./gui/sayHelloWidget.ui', self)
        self.btn.clicked.connect(self.sayHello)

    def sayHello(self):
        inputTxt = self.input.text()
        self.output.setText(f'Hello There {inputTxt}')
