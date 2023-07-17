from PyQt6.QtWidgets import QMainWindow, QLabel

def decode_model(results):
    for k in results:
        if type(results[k])==bytes:
            results[k]=results[k].decode('utf-8')
    return results

def create_ui_message_box(msg):
    messageBox = QMainWindow()
    label = QLabel(str(msg))
    label.setStyleSheet('font-size:24px;padding:20px;')
    messageBox.setCentralWidget(label)
    return messageBox