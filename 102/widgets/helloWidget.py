from PyQt6.QtWidgets import QWidget, QScrollArea
from PyQt6 import uic, QtGui
import MySQLdb as mdb

class HelloWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./gui/sayHelloWidget.ui', self)
        self.btn.clicked.connect(self.sayHello)

    def sayHello(self):
        inputTxt = self.input.text()
        message = f'Hello There {inputTxt}'
        connnection = mdb.connect('localhost','root','root','pyqt6')
        with connnection:
            cur = connnection.cursor()
            cur.execute("INSERT INTO hellos(name,message) VALUES('%s','%s')" % (''.join(inputTxt),''.join(message)))
            print('data eneterd')
        self.output.setText(f'"{message}": Created')


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