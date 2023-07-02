from PyQt6.QtWidgets import QMainWindow, QLabel

def decode_model(results):
    return {k: v.decode("utf-8") for k,v in results.items()}

def create_ui_message_box(msg):
    messageBox = QMainWindow()
    label = QLabel(str(msg))
    label.setStyleSheet('font-size:24px;padding:20px;')
    messageBox.setCentralWidget(label)
    return messageBox