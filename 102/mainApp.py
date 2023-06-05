import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import Qt
from PyQt6 import uic

# My Widgets
from widgets.leftDock import LeftDock
from widgets.helloWidget import HelloWidget
from widgets.mainWidget import MainWidget as main

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/mainWindow.ui', self)

        # Adding docking widgets
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, LeftDock())
        
        # Adding the Main Widget
        self.setCentralWidget(main())



# Launching Application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()


# Closing Application
try:
    sys.exit(app.exec())
except SystemExit:
    print('Goodbye...')