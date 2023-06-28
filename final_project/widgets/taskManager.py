from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

class TaskManager(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('views/taskManagement.ui', self)

        self.titleLabel.setProperty('class','label')
        self.titleInput.setProperty('class','input')
        self.descriptionLabel.setProperty('class','label')
        self.descriptionInput.setProperty('class','input')