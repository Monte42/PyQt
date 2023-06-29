from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class ChoreManager(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('views/choreManagement.ui', self)

        self.personLabel.setProperty('class','label')
        self.personInput.setProperty('class','input')
        self.taskLabel.setProperty('class','label')
        self.taskInput.setProperty('class','input')
        self.notesLabel.setProperty('class','label')
        self.notesInput.setProperty('class','input')