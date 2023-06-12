import sys
from PyQt6.QtWidgets import QScrollArea

class MainWidget(QScrollArea):
    def __init__(self, widget):
        super().__init__()
        self.setWidget(widget())
