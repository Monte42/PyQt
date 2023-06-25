import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QHBoxLayout,QLabel
from PyQt6 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        # =========
        # Method 1 - Apply to a widget
        # =========
        # Applying styleSheets to a sigle element will only
        # affect that element
        self.sweet.setStyleSheet('font-size:20px;')

        # Use setProperty to set classes to elements for 
        #   shared style between specific elements.
        # *** Style found in 'styles.css' file ***
        self.hiddenBtn.setProperty('class', 'danger')

        # opening second window 
        self.dude.clicked.connect(self.openWindow)


    def openWindow(self):
        popup = QMainWindow()
        layout = QHBoxLayout()
        label = QLabel("Hello World!", parent=popup)
        label.resize(200,75)

        # =========
        # Method 2 - Apply to a window
        # =========
        # Applying a stylesheet to a window will only affect
        # related elements in that window.
        popup.setStyleSheet("""
            QMainWindow{
                background-color: #333;
                color: white;
            }
            QLabel{
                padding-left: 20px;
                font-family: Script;
                font-size: 24px;
            }
        """)

        self.popup = popup
        self.popup.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # =========
    # Method 3 - Apply to the application
    # =========

    # Applying a stylesheet to the QApplication, the style will
    # apply to every related element in every window
    # app.setStyleSheet("""
    #     QMainWindow{
    #         background-color: #469;
    #     }
    #     QLabel{
    #         color:white;
    #         font-size:25px;
    #         width: fit-content;
    #         font-family: ink free;
    #     }
    #     QPushButton{
    #         color: yellow;
    #     }
    #     #dude{
    #         background-color: red;
    #     }
    #     #sweet{
    #         background-color: green;
    #     }
    #   .danger{ <-- THIS IS THE ABOVE CLASS **
    #       background-color: red;
    #       color: white;
    #   }
    # """)



    # =========
    # Method 4 - Apply to a widget using a .css file
    # =========

    #  Stylesheets can be made like normal css and imported to help 
    #   keep projects clean. ***This replace the above block of code

    # First    'open' and 'read' the file
    # Second   store it in a var
    # Third    pass the var in the style and call .read() on the var
    with open('styles.css', 'r') as file:
        app.setStyleSheet(file.read())

    main = MainWindow()
    main.show()

try:
    sys.exit(app.exec())
except:
    print('Goodbye...')