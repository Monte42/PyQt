# Form implementation generated from reading ui file 'g:\Documents\PyQt\final_project\views\userManagement.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_userNamangementWindow(object):
    def setupUi(self, userNamangementWindow):
        userNamangementWindow.setObjectName("userNamangementWindow")
        userNamangementWindow.resize(332, 163)
        self.usernameLabel = QtWidgets.QLabel(parent=userNamangementWindow)
        self.usernameLabel.setGeometry(QtCore.QRect(20, 60, 91, 21))
        self.usernameLabel.setObjectName("usernameLabel")
        self.usernameInput = QtWidgets.QLineEdit(parent=userNamangementWindow)
        self.usernameInput.setGeometry(QtCore.QRect(120, 60, 191, 22))
        self.usernameInput.setObjectName("usernameInput")
        self.passwordInput = QtWidgets.QLineEdit(parent=userNamangementWindow)
        self.passwordInput.setGeometry(QtCore.QRect(120, 90, 191, 22))
        self.passwordInput.setText("")
        self.passwordInput.setObjectName("passwordInput")
        self.passwordLabel = QtWidgets.QLabel(parent=userNamangementWindow)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 90, 91, 21))
        self.passwordLabel.setObjectName("passwordLabel")
        self.mainHeader = QtWidgets.QLabel(parent=userNamangementWindow)
        self.mainHeader.setGeometry(QtCore.QRect(20, 20, 291, 31))
        self.mainHeader.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.mainHeader.setObjectName("mainHeader")
        self.submitBtn = QtWidgets.QPushButton(parent=userNamangementWindow)
        self.submitBtn.setGeometry(QtCore.QRect(220, 120, 93, 28))
        self.submitBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.submitBtn.setObjectName("submitBtn")

        self.retranslateUi(userNamangementWindow)
        QtCore.QMetaObject.connectSlotsByName(userNamangementWindow)

    def retranslateUi(self, userNamangementWindow):
        _translate = QtCore.QCoreApplication.translate
        userNamangementWindow.setWindowTitle(_translate("userNamangementWindow", "User Management"))
        self.usernameLabel.setText(_translate("userNamangementWindow", "Username"))
        self.passwordLabel.setText(_translate("userNamangementWindow", "Password"))
        self.mainHeader.setText(_translate("userNamangementWindow", "Enter Credentials"))
        self.submitBtn.setText(_translate("userNamangementWindow", "Submit"))