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
        calculator.resize(209, 343)
        calculator.setMinimumSize(QtCore.QSize(200, 271))
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.display = QtWidgets.QTextEdit(parent=self.dockWidgetContents)
        self.display.setObjectName("display")
        self.gridLayout.addWidget(self.display, 0, 0, 1, 4)
        self.btn_1 = QtWidgets.QPushButton(parent=self.dockWidgetContents)
        self.btn_1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 1, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(parent=self.dockWidgetContents)
        self.btn_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 1, 1, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(parent=self.dockWidgetContents)
        self.btn_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 1, 2, 1, 1)
        self.addBtn = QtWidgets.QPushButton(parent=self.dockWidgetContents)
        self.addBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.addBtn.setObjectName("addBtn")
        self.gridLayout.addWidget(self.addBtn, 1, 3, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(parent=self.dockWidgetContents)
        self.btn_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(parent=self.dockWidgetContents)
        self.btn_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(parent=self.dockWidgetContents)
        self.btn_6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)
        self.subtractBtn = QtWidgets.QPushButton(parent=self.dockWidgetContents)
        self.subtractBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.subtractBtn.setObjectName("subtractBtn")
        self.gridLayout.addWidget(self.subtractBtn, 2, 3, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(parent=self.dockWidgetContents)
        self.btn_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 3, 0, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(parent=self.dockWidgetContents)
        self.btn_8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 3, 1, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(parent=self.dockWidgetContents)
        self.btn_9.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 3, 2, 1, 1)
        self.multiplyBtn = QtWidgets.QPushButton(parent=self.dockWidgetContents)
        self.multiplyBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.multiplyBtn.setObjectName("multiplyBtn")
        self.gridLayout.addWidget(self.multiplyBtn, 3, 3, 1, 1)
        self.bt_dot = QtWidgets.QPushButton(parent=self.dockWidgetContents)
        self.bt_dot.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_dot.setObjectName("bt_dot")
        self.gridLayout.addWidget(self.bt_dot, 4, 0, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(parent=self.dockWidgetContents)
        self.btn_0.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 4, 1, 1, 1)
        self.equalsBtn = QtWidgets.QPushButton(parent=self.dockWidgetContents)
        self.equalsBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.equalsBtn.setObjectName("equalsBtn")
        self.gridLayout.addWidget(self.equalsBtn, 4, 2, 1, 1)
        self.divideBtn = QtWidgets.QPushButton(parent=self.dockWidgetContents)
        self.divideBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.divideBtn.setObjectName("divideBtn")
        self.gridLayout.addWidget(self.divideBtn, 4, 3, 1, 1)
        calculator.setWidget(self.dockWidgetContents)

        self.retranslateUi(calculator)
        QtCore.QMetaObject.connectSlotsByName(calculator)

    def retranslateUi(self, calculator):
        _translate = QtCore.QCoreApplication.translate
        calculator.setWindowTitle(_translate("calculator", "Calculator"))
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
