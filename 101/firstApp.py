from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import sys


# QMainWindow - ever app needs one, but can have more than one
    # Main focus for user of app
    # App will run until last main window is closed

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Set Window Attr
        self.setWindowTitle('Mr 636')
        self.resize(500, 350)

        # Create layout obj, set class layout attr to new obj
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create Widgets
        self.inputField = QLineEdit()
        button = QPushButton('Say &Hello', clicked=self.sayHello)
        self.output = QTextEdit()

        # Add wdigets to Layout
        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)

    # Create a class method to run when triggered by an event
    def sayHello(self):
        inputText = self.inputField.text()
        self.output.setText(f'Hello {inputText}')


# QApplication - every Qt App needs one, and only one.
    # The QApplication class is an event loop. The event
    # loop waits for events, ques the events and passes them
    # to the event hanldler and then back to the client

# creating the event loop
app = QApplication(sys.argv) # sys.argv enables cmd line arguments
                            # Pass empty [] if you know there wont be args 

# Adding CSS
app.setStyleSheet(
        '''
        QWidget{
            font-size: 45px;
        }
        QPushButton{
            font-size: 20px;
        }
        '''
    )


# Create a class instance of MainWindow
window = MainWindow()



# Render the window class instance
window.show()


# activating the application
sys.exit(app.exec())