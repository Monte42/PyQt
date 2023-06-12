import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import Qt
from PyQt6 import uic

# My Widgets
from widgets.leftDock import LeftDock
from widgets.rightDock import RightDock
from widgets.bottomDock import BottomDock
from widgets.mainWidget import MainWidget as main
from widgets.helloWidget import HelloWidget

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/mainWindow.ui', self)
        self.resize(1700,1000)
        
        self.clearWorkspace.triggered.connect(self.clearApp)
        self.fontDefault.triggered.connect(self.clearApp)
        self.sizeDefault.triggered.connect(self.clearApp)
        self.fontCambria.triggered.connect(self.updateFontCambria)
        self.fontInkFree.triggered.connect(self.updateFontInkFree)
        self.fontBoli.triggered.connect(self.updateFontBoli)
        self.font16.triggered.connect(self.updateFont16)
        self.font18.triggered.connect(self.updateFont18)
        self.font22.triggered.connect(self.updateFont22)
        self.showSideMenu.triggered.connect(self.showLeftDock)
        self.showBottomDock.triggered.connect(self.showBottomForm)
        self.showRightDock.triggered.connect(self.showRightForm)


        # Adding docking widgets
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, LeftDock())
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, BottomDock())
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, RightDock())
        
        # Adding the Main Widget
        self.setCentralWidget(main(HelloWidget))

    def clearApp(self):
        self.setCentralWidget(main(HelloWidget))
    def updateFontCambria(self):
        self.setCentralWidget(HelloWidget.updateFont(HelloWidget(),"Cambria Math"))
    def updateFontInkFree(self):
        self.setCentralWidget(HelloWidget.updateFont(HelloWidget(),"Ink Free"))
    def updateFontBoli(self):
        self.setCentralWidget(HelloWidget.updateFont(HelloWidget(),"MV Boli"))
    def updateFont16(self):
        self.setCentralWidget(HelloWidget.updateFontsize(HelloWidget(),16))
    def updateFont18(self):
        self.setCentralWidget(HelloWidget.updateFontsize(HelloWidget(),18))
    def updateFont22(self):
        self.setCentralWidget(HelloWidget.updateFontsize(HelloWidget(),22))
    def showLeftDock(self):
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, LeftDock())
    def showBottomForm(self):
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, BottomDock())
    def showRightForm(self):
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, RightDock())
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