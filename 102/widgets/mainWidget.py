import sys
from PyQt6.QtWidgets import QScrollArea
from .helloWidget import HelloWidget as w

class MainWidget(QScrollArea):
    def __init__(self):
        super().__init__()
        self.setWidget(w())
