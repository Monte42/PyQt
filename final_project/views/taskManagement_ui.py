# Form implementation generated from reading ui file 'g:\Documents\PyQt\final_project\views\taskManagement.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_newTaskWindow(object):
    def setupUi(self, newTaskWindow):
        newTaskWindow.setObjectName("newTaskWindow")
        newTaskWindow.resize(306, 294)
        self.submitBtn = QtWidgets.QPushButton(parent=newTaskWindow)
        self.submitBtn.setGeometry(QtCore.QRect(200, 250, 93, 28))
        self.submitBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.submitBtn.setObjectName("submitBtn")
        self.titleInput = QtWidgets.QLineEdit(parent=newTaskWindow)
        self.titleInput.setGeometry(QtCore.QRect(20, 90, 271, 31))
        self.titleInput.setObjectName("titleInput")
        self.descriptionInput = QtWidgets.QPlainTextEdit(parent=newTaskWindow)
        self.descriptionInput.setGeometry(QtCore.QRect(20, 150, 271, 81))
        self.descriptionInput.setObjectName("descriptionInput")
        self.titleLabel = QtWidgets.QLabel(parent=newTaskWindow)
        self.titleLabel.setGeometry(QtCore.QRect(20, 60, 161, 21))
        self.titleLabel.setObjectName("titleLabel")
        self.descriptionLabel = QtWidgets.QLabel(parent=newTaskWindow)
        self.descriptionLabel.setGeometry(QtCore.QRect(20, 130, 191, 21))
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.mainHeader = QtWidgets.QLabel(parent=newTaskWindow)
        self.mainHeader.setGeometry(QtCore.QRect(20, 20, 271, 31))
        self.mainHeader.setObjectName("mainHeader")

        self.retranslateUi(newTaskWindow)
        QtCore.QMetaObject.connectSlotsByName(newTaskWindow)

    def retranslateUi(self, newTaskWindow):
        _translate = QtCore.QCoreApplication.translate
        newTaskWindow.setWindowTitle(_translate("newTaskWindow", "Task Management"))
        self.submitBtn.setText(_translate("newTaskWindow", "Submit"))
        self.titleLabel.setText(_translate("newTaskWindow", "Title"))
        self.descriptionLabel.setText(_translate("newTaskWindow", "Description"))
        self.mainHeader.setText(_translate("newTaskWindow", "Task Management"))
