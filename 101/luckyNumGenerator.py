# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUIs\luckyNumGenerator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import random

WB_START = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
WB_TITLE = "<h1>Your #'s</h1>\n"
WB_END = "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(347, 462)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(self.centralwidget, clicked=self.onTriggerEvent)
        self.btn.setGeometry(QtCore.QRect(20, 100, 281, 71))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(22)
        self.btn.setFont(font)
        self.btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn.setObjectName("btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 25, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.txtBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.txtBox.setGeometry(QtCore.QRect(20, 180, 281, 192))
        self.txtBox.setObjectName("txtBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 347, 26))
        self.menubar.setObjectName("menubar")
        self.menuYurp = QtWidgets.QMenu(self.menubar)
        self.menuYurp.setObjectName("menuYurp")
        self.menuMaybe = QtWidgets.QMenu(self.menuYurp)
        self.menuMaybe.setObjectName("menuMaybe")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionYes = QtWidgets.QAction(MainWindow)
        self.actionYes.setObjectName("actionYes")
        self.actionNo = QtWidgets.QAction(MainWindow)
        self.actionNo.setObjectName("actionNo")
        self.actionNo_2 = QtWidgets.QAction(MainWindow)
        self.actionNo_2.setObjectName("actionNo_2")
        self.actionYes_2 = QtWidgets.QAction(MainWindow)
        self.actionYes_2.setObjectName("actionYes_2")
        self.menuMaybe.addAction(self.actionNo_2)
        self.menuMaybe.addAction(self.actionYes_2)
        self.menuYurp.addAction(self.actionYes)
        self.menuYurp.addAction(self.actionNo)
        self.menuYurp.addSeparator()
        self.menuYurp.addAction(self.menuMaybe.menuAction())
        self.menubar.addAction(self.menuYurp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mr636"))
        self.btn.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "Your Lucky #\'$"))
        self.txtBox.setHtml(_translate("MainWindow", f'{WB_START}{WB_TITLE}{WB_END}'))
        self.menuYurp.setTitle(_translate("MainWindow", "Yurp"))
        self.menuMaybe.setTitle(_translate("MainWindow", "Maybe?"))
        self.actionYes.setText(_translate("MainWindow", "Yes"))
        self.actionNo.setText(_translate("MainWindow", "No"))
        self.actionNo_2.setText(_translate("MainWindow", "No"))
        self.actionYes_2.setText(_translate("MainWindow", "Yes"))

    def onTriggerEvent(self):
        num = ''
        for i in range(6):
            num += f'{random.randint(0, 99)}' if i == 0 else f'-{random.randint(0, 99)}' 
        self.txtBox.setHtml(f'{WB_START}{WB_TITLE}"<h2>{num}</h2>\n"{WB_END}')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
