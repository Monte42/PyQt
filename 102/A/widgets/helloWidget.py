from PyQt6.QtWidgets import QWidget, QScrollArea
from PyQt6 import uic, QtGui

class HelloWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./gui/sayHelloWidget.ui', self)
        self.btn.clicked.connect(self.sayHello)

    def sayHello(self):
        inputTxt = self.input.text()
        message = f'Hello There {inputTxt}'
        self.output.setText(message)


    def updateFont(self,fontfamily):
        font = QtGui.QFont()
        font.setFamily(fontfamily)
        font.setPointSize(20)
        self.input.setFont(font)
        self.btn.setFont(font)
        self.output.setFont(font)
        return self.window()

    def updateFontsize(self,size):
        font = QtGui.QFont()
        font.setPointSize(size)
        self.input.setFont(font)
        self.btn.setFont(font)
        self.output.setFont(font)
        return self.window()