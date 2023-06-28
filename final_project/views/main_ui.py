# Form implementation generated from reading ui file 'g:\Documents\PyQt\final_project\views\main.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 689)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainHeader = QtWidgets.QLabel(parent=self.centralwidget)
        self.mainHeader.setGeometry(QtCore.QRect(20, 10, 321, 51))
        self.mainHeader.setObjectName("mainHeader")
        self.notesHeader = QtWidgets.QLabel(parent=self.centralwidget)
        self.notesHeader.setGeometry(QtCore.QRect(20, 380, 321, 41))
        self.notesHeader.setObjectName("notesHeader")
        self.choreList = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.choreList.setGeometry(QtCore.QRect(20, 50, 321, 331))
        self.choreList.setTabKeyNavigation(True)
        self.choreList.setProperty("showDropIndicator", True)
        self.choreList.setAlternatingRowColors(True)
        self.choreList.setShowGrid(True)
        self.choreList.setObjectName("choreList")
        self.choreList.setColumnCount(4)
        self.choreList.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.choreList.setItem(3, 3, item)
        self.choreList.verticalHeader().setVisible(False)
        self.notesDisplay = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.notesDisplay.setEnabled(False)
        self.notesDisplay.setGeometry(QtCore.QRect(20, 420, 321, 221))
        font = QtGui.QFont()
        font.setFamily("Script")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.notesDisplay.setFont(font)
        self.notesDisplay.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.notesDisplay.setObjectName("notesDisplay")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 26))
        self.menubar.setObjectName("menubar")
        self.menuTools = QtWidgets.QMenu(parent=self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.showCalculator = QtGui.QAction(parent=MainWindow)
        self.showCalculator.setObjectName("showCalculator")
        self.enterAdmin = QtGui.QAction(parent=MainWindow)
        self.enterAdmin.setObjectName("enterAdmin")
        self.menuTools.addAction(self.showCalculator)
        self.menuTools.addAction(self.enterAdmin)
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Family Planner"))
        self.mainHeader.setText(_translate("MainWindow", "Your Chores"))
        self.notesHeader.setText(_translate("MainWindow", "Speacil Notes"))
        item = self.choreList.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.choreList.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.choreList.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.choreList.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.choreList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ChoreID"))
        item = self.choreList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Task"))
        item = self.choreList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Due Date"))
        item = self.choreList.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Completed"))
        __sortingEnabled = self.choreList.isSortingEnabled()
        self.choreList.setSortingEnabled(False)
        item = self.choreList.item(0, 0)
        item.setText(_translate("MainWindow", "412"))
        item = self.choreList.item(0, 1)
        item.setText(_translate("MainWindow", "Take Out Trash"))
        item = self.choreList.item(0, 2)
        item.setText(_translate("MainWindow", "07/05"))
        item = self.choreList.item(0, 3)
        item.setText(_translate("MainWindow", "Yes"))
        item = self.choreList.item(1, 0)
        item.setText(_translate("MainWindow", "415"))
        item = self.choreList.item(1, 1)
        item.setText(_translate("MainWindow", "Clean Kitchen"))
        item = self.choreList.item(1, 2)
        item.setText(_translate("MainWindow", "07/10"))
        item = self.choreList.item(1, 3)
        item.setText(_translate("MainWindow", "No"))
        item = self.choreList.item(2, 0)
        item.setText(_translate("MainWindow", "416"))
        item = self.choreList.item(2, 1)
        item.setText(_translate("MainWindow", "Clean Room"))
        item = self.choreList.item(2, 2)
        item.setText(_translate("MainWindow", "07/10"))
        item = self.choreList.item(2, 3)
        item.setText(_translate("MainWindow", "No"))
        item = self.choreList.item(3, 0)
        item.setText(_translate("MainWindow", "419"))
        item = self.choreList.item(3, 1)
        item.setText(_translate("MainWindow", "Water Plants"))
        item = self.choreList.item(3, 2)
        item.setText(_translate("MainWindow", "07/05"))
        item = self.choreList.item(3, 3)
        item.setText(_translate("MainWindow", "Yes"))
        self.choreList.setSortingEnabled(__sortingEnabled)
        self.notesDisplay.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Script\'; font-size:17pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Make sure to get the upstairs bathrooms too</p></body></html>"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.showCalculator.setText(_translate("MainWindow", "Calculator"))
        self.enterAdmin.setText(_translate("MainWindow", "Enter Admin"))
