# Form implementation generated from reading ui file 'g:\Documents\PyQt\final_project\views\newChore.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_choreManagementWindow(object):
    def setupUi(self, choreManagementWindow):
        choreManagementWindow.setObjectName("choreManagementWindow")
        choreManagementWindow.resize(354, 401)
        self.centralwidget = QtWidgets.QWidget(parent=choreManagementWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.person = QtWidgets.QComboBox(parent=self.centralwidget)
        self.person.setGeometry(QtCore.QRect(20, 90, 141, 31))
        self.person.setObjectName("person")
        self.task = QtWidgets.QComboBox(parent=self.centralwidget)
        self.task.setGeometry(QtCore.QRect(180, 90, 141, 31))
        self.task.setObjectName("task")
        self.personLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.personLabel.setGeometry(QtCore.QRect(20, 60, 141, 21))
        self.personLabel.setObjectName("personLabel")
        self.taskLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.taskLabel.setGeometry(QtCore.QRect(180, 60, 141, 21))
        self.taskLabel.setObjectName("taskLabel")
        self.mainHeader = QtWidgets.QLabel(parent=self.centralwidget)
        self.mainHeader.setGeometry(QtCore.QRect(20, 10, 251, 41))
        self.mainHeader.setObjectName("mainHeader")
        self.date = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.date.setGeometry(QtCore.QRect(100, 130, 221, 31))
        self.date.setObjectName("date")
        self.dateLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(20, 130, 81, 31))
        self.dateLabel.setObjectName("dateLabel")
        self.notesLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.notesLabel.setGeometry(QtCore.QRect(20, 170, 121, 31))
        self.notesLabel.setObjectName("notesLabel")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 200, 311, 101))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 310, 81, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 310, 93, 28))
        self.pushButton.setObjectName("pushButton")
        choreManagementWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=choreManagementWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 354, 26))
        self.menubar.setObjectName("menubar")
        self.menuTools = QtWidgets.QMenu(parent=self.menubar)
        self.menuTools.setObjectName("menuTools")
        choreManagementWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=choreManagementWindow)
        self.statusbar.setObjectName("statusbar")
        choreManagementWindow.setStatusBar(self.statusbar)
        self.actionCreate_New_Chore = QtGui.QAction(parent=choreManagementWindow)
        self.actionCreate_New_Chore.setObjectName("actionCreate_New_Chore")
        self.actionCreate_New_Profile = QtGui.QAction(parent=choreManagementWindow)
        self.actionCreate_New_Profile.setObjectName("actionCreate_New_Profile")
        self.menuTools.addAction(self.actionCreate_New_Chore)
        self.menuTools.addAction(self.actionCreate_New_Profile)
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(choreManagementWindow)
        QtCore.QMetaObject.connectSlotsByName(choreManagementWindow)

    def retranslateUi(self, choreManagementWindow):
        _translate = QtCore.QCoreApplication.translate
        choreManagementWindow.setWindowTitle(_translate("choreManagementWindow", "Chore Management"))
        self.personLabel.setText(_translate("choreManagementWindow", "Person"))
        self.taskLabel.setText(_translate("choreManagementWindow", "Task"))
        self.mainHeader.setText(_translate("choreManagementWindow", "Chore Management"))
        self.dateLabel.setText(_translate("choreManagementWindow", "Due Date"))
        self.notesLabel.setText(_translate("choreManagementWindow", "Special Notes"))
        self.label.setText(_translate("choreManagementWindow", "0/250"))
        self.pushButton.setText(_translate("choreManagementWindow", "Create"))
        self.menuTools.setTitle(_translate("choreManagementWindow", "Tools"))
        self.actionCreate_New_Chore.setText(_translate("choreManagementWindow", "Create New Chore"))
        self.actionCreate_New_Profile.setText(_translate("choreManagementWindow", "Create New Profile"))