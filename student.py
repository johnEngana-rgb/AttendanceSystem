# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Student_sheet(object):
    def setupUi(self, Student_sheet):
        Student_sheet.setObjectName("Student_sheet")
        Student_sheet.resize(1282, 716)
        Student_sheet.setStyleSheet("QWidget#MainWindow{\n"
"background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.911, y2:1, stop:0 rgba(79, 255, 159, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.centralwidget = QtWidgets.QWidget(Student_sheet)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 2, 8, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 3, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 3, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 5, 0, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 6, 0, 1, 2)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 7, 0, 1, 2)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 8, 0, 1, 3)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 9, 0, 1, 3)
        Student_sheet.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Student_sheet)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1282, 26))
        self.menubar.setObjectName("menubar")
        Student_sheet.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Student_sheet)
        self.statusbar.setObjectName("statusbar")
        Student_sheet.setStatusBar(self.statusbar)

        self.retranslateUi(Student_sheet)
        QtCore.QMetaObject.connectSlotsByName(Student_sheet)

    def retranslateUi(self, Student_sheet):
        _translate = QtCore.QCoreApplication.translate
        Student_sheet.setWindowTitle(_translate("Student_sheet", "MainWindow"))
        self.lineEdit.setText(_translate("Student_sheet", "Student ID"))
        self.lineEdit.setPlaceholderText(_translate("Student_sheet", "First Name"))
        self.lineEdit_2.setText(_translate("Student_sheet", "First Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Student_sheet", "First Name"))
        self.lineEdit_3.setText(_translate("Student_sheet", "Last Name"))
        self.lineEdit_3.setPlaceholderText(_translate("Student_sheet", "First Name"))
        self.comboBox.setItemText(0, _translate("Student_sheet", "M"))
        self.comboBox.setItemText(1, _translate("Student_sheet", "F"))
        self.comboBox_2.setItemText(0, _translate("Student_sheet", "1st Year"))
        self.comboBox_2.setItemText(1, _translate("Student_sheet", "2nd Year"))
        self.comboBox_2.setItemText(2, _translate("Student_sheet", "3rd Year"))
        self.comboBox_2.setItemText(3, _translate("Student_sheet", "4th Year"))
        self.pushButton.setText(_translate("Student_sheet", "Add Student"))
        self.pushButton_2.setText(_translate("Student_sheet", "Delete Student"))
        self.pushButton_3.setText(_translate("Student_sheet", "Edit Student"))
        self.pushButton_4.setText(_translate("Student_sheet", "Home Button"))
        self.pushButton_6.setText(_translate("Student_sheet", "VIEW ACTIVITIES"))
        self.pushButton_5.setText(_translate("Student_sheet", "TAKE ATTENDANCE"))
