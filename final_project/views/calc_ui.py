# Form implementation generated from reading ui file 'g:\Documents\PyQt\final_project\views\calc.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_calculator(object):
    def setupUi(self, calculator):
        calculator.setObjectName("calculator")
        calculator.resize(200, 484)
        calculator.setMinimumSize(QtCore.QSize(200, 400))
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.historyLabel = QtWidgets.QLabel(parent=self.dockWidgetContents)
        self.historyLabel.setObjectName("historyLabel")
        self.gridLayout_2.addWidget(self.historyLabel, 0, 0, 1, 1)
        self.historyList = QtWidgets.QListWidget(parent=self.dockWidgetContents)
        self.historyList.setEnabled(False)
        self.historyList.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.historyList.setAlternatingRowColors(False)
        self.historyList.setObjectName("historyList")
        item = QtWidgets.QListWidgetItem()
        self.historyList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.historyList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.historyList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.historyList.addItem(item)
        self.gridLayout_2.addWidget(self.historyList, 1, 0, 1, 1)
        self.display = QtWidgets.QLineEdit(parent=self.dockWidgetContents)
        self.display.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.display.setFont(font)
        self.display.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.display.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.display.setObjectName("display")
        self.gridLayout_2.addWidget(self.display, 2, 0, 1, 1)
        self.keypad = QtWidgets.QFrame(parent=self.dockWidgetContents)
        self.keypad.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.keypad.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.keypad.setObjectName("keypad")
        self.gridLayout = QtWidgets.QGridLayout(self.keypad)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_1 = QtWidgets.QPushButton(parent=self.keypad)
        self.btn_1.setMaximumSize(QtCore.QSize(100, 50))
        self.btn_1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 0, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(parent=self.keypad)
        self.btn_2.setMaximumSize(QtCore.QSize(100, 50))
        self.btn_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 0, 1, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(parent=self.keypad)
        self.btn_3.setMaximumSize(QtCore.QSize(100, 50))
        self.btn_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 0, 2, 1, 1)
        self.addBtn = QtWidgets.QPushButton(parent=self.keypad)
        self.addBtn.setMaximumSize(QtCore.QSize(100, 50))
        self.addBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.addBtn.setObjectName("addBtn")
        self.gridLayout.addWidget(self.addBtn, 0, 3, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(parent=self.keypad)
        self.btn_4.setMaximumSize(QtCore.QSize(100, 50))
        self.btn_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 1, 0, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(parent=self.keypad)
        self.btn_5.setMaximumSize(QtCore.QSize(100, 50))
        self.btn_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 1, 1, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(parent=self.keypad)
        self.btn_6.setMaximumSize(QtCore.QSize(100, 50))
        self.btn_6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 1, 2, 1, 1)
        self.subtractBtn = QtWidgets.QPushButton(parent=self.keypad)
        self.subtractBtn.setMaximumSize(QtCore.QSize(100, 50))
        self.subtractBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.subtractBtn.setObjectName("subtractBtn")
        self.gridLayout.addWidget(self.subtractBtn, 1, 3, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(parent=self.keypad)
        self.btn_7.setMaximumSize(QtCore.QSize(100, 50))
        self.btn_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 2, 0, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(parent=self.keypad)
        self.btn_8.setMaximumSize(QtCore.QSize(100, 50))
        self.btn_8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 2, 1, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(parent=self.keypad)
        self.btn_9.setMaximumSize(QtCore.QSize(100, 50))
        self.btn_9.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 2, 2, 1, 1)
        self.multiplyBtn = QtWidgets.QPushButton(parent=self.keypad)
        self.multiplyBtn.setMaximumSize(QtCore.QSize(100, 50))
        self.multiplyBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.multiplyBtn.setObjectName("multiplyBtn")
        self.gridLayout.addWidget(self.multiplyBtn, 2, 3, 1, 1)
        self.bt_dot = QtWidgets.QPushButton(parent=self.keypad)
        self.bt_dot.setMaximumSize(QtCore.QSize(100, 50))
        self.bt_dot.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_dot.setObjectName("bt_dot")
        self.gridLayout.addWidget(self.bt_dot, 3, 0, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(parent=self.keypad)
        self.btn_0.setMaximumSize(QtCore.QSize(100, 50))
        self.btn_0.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 3, 1, 1, 1)
        self.equalsBtn = QtWidgets.QPushButton(parent=self.keypad)
        self.equalsBtn.setMaximumSize(QtCore.QSize(100, 50))
        self.equalsBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.equalsBtn.setObjectName("equalsBtn")
        self.gridLayout.addWidget(self.equalsBtn, 3, 2, 1, 1)
        self.divideBtn = QtWidgets.QPushButton(parent=self.keypad)
        self.divideBtn.setMaximumSize(QtCore.QSize(100, 50))
        self.divideBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.divideBtn.setObjectName("divideBtn")
        self.gridLayout.addWidget(self.divideBtn, 3, 3, 1, 1)
        self.gridLayout_2.addWidget(self.keypad, 3, 0, 1, 1)
        calculator.setWidget(self.dockWidgetContents)

        self.retranslateUi(calculator)
        QtCore.QMetaObject.connectSlotsByName(calculator)

    def retranslateUi(self, calculator):
        _translate = QtCore.QCoreApplication.translate
        calculator.setWindowTitle(_translate("calculator", "Calculator"))
        self.historyLabel.setText(_translate("calculator", "History"))
        self.historyList.setStatusTip(_translate("calculator", "Display Only"))
        __sortingEnabled = self.historyList.isSortingEnabled()
        self.historyList.setSortingEnabled(False)
        item = self.historyList.item(0)
        item.setText(_translate("calculator", "10+12=22"))
        item = self.historyList.item(1)
        item.setText(_translate("calculator", "22+13=35"))
        item = self.historyList.item(2)
        item.setText(_translate("calculator", "35*2=70"))
        item = self.historyList.item(3)
        item.setText(_translate("calculator", "20-8=12"))
        self.historyList.setSortingEnabled(__sortingEnabled)
        self.display.setStatusTip(_translate("calculator", "Display Only"))
        self.display.setText(_translate("calculator", "74812149"))
        self.btn_1.setText(_translate("calculator", "1"))
        self.btn_2.setText(_translate("calculator", "2"))
        self.btn_3.setText(_translate("calculator", "3"))
        self.addBtn.setText(_translate("calculator", "+"))
        self.btn_4.setText(_translate("calculator", "4"))
        self.btn_5.setText(_translate("calculator", "5"))
        self.btn_6.setText(_translate("calculator", "6"))
        self.subtractBtn.setText(_translate("calculator", "-"))
        self.btn_7.setText(_translate("calculator", "7"))
        self.btn_8.setText(_translate("calculator", "8"))
        self.btn_9.setText(_translate("calculator", "9"))
        self.multiplyBtn.setText(_translate("calculator", "*"))
        self.bt_dot.setText(_translate("calculator", "."))
        self.btn_0.setText(_translate("calculator", "0"))
        self.equalsBtn.setText(_translate("calculator", "="))
        self.divideBtn.setText(_translate("calculator", "/"))