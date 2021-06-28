import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, QDate, QTime, Qt
from PyQt5.QtGui import *
import sqlite3
from Main import Ui_A
from hom import Ui_MainWindow
from activity import Ui_act
from student import Ui_Student_sheet
import PyQt5


class MainWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWin, self).__init__(parent=None)
        self.setupUi(self)
        self.show()
        self.attendance_button()
        self.activity_btn()
        self.student_btn()

    def attendance_button(self):
        self.close()
        self.pushButton_2.clicked.connect(self.attendance)

    def activity_btn(self):
        self.pushButton.clicked.connect(self.activity)

    def student_btn(self):
        self.pushButton_3.clicked.connect(self.student)

    def attendance(self):
        self.close()
        self.newWin = AttendanceWin()
        self.newWin.show()

    def student(self):
        self.close()
        self.studWin = studentWin()
        self.studWin.show()

    def activity(self):
        self.close()
        self.newWin = ActivityWin()
        self.newWin.show()


class studentWin(QtWidgets.QMainWindow, Ui_Student_sheet):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.load_students()
        self.home_btn()
        self.add_btn()
        self.del_btn()
        self.act_btn()
        self.att_btn()

    def home_btn(self):
        self.pushButton_4.clicked.connect(self.home)

    def home(self):
        self.close()
        self.newWin = MainWin()
        self.newWin.show()

    def del_btn(self):
        self.pushButton_2.clicked.connect(self.del_stud)

    def add_btn(self):
        self.pushButton.clicked.connect(self.add_stud)

    def act_btn(self):
        self.pushButton_6.clicked.connect(self.activities)

    def att_btn(self):
        self.pushButton_5.clicked.connect(self.attendance)

    def attendance(self):
        self.close()
        self.newWin = AttendanceWin()
        self.newWin.show()

    def activities(self):
        self.close()
        self.newWin = ActivityWin()
        self.newWin.show()

    def del_stud(self):
        print("pushed del")
        sel = str(self.tableWidget.currentItem().text())
        conn = sqlite3.connect('attendance.db')
        c = conn.cursor()
        print(sel)
        c.execute("DELETE FROM students WHERE student_id = (?)", (sel,))

        result = c.execute("SELECT* FROM students")

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        conn.commit()
        c.close()

    def add_stud(self):
        conn = sqlite3.connect('attendance.db')
        c = conn.cursor()
        id = self.lineEdit.text()
        fname = self.lineEdit_2.text()
        lnamme = self.lineEdit_3.text()
        year = str(self.comboBox_2.currentText())
        course = (self.comboBox.currentText())
        student_info = [(id, fname, lnamme, year, course)]
        with conn:
            print("pushed")
            c.executemany("INSERT INTO students VALUES(?,?,?,?,?)", student_info)

        result = c.execute("SELECT* FROM students")
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        conn.commit()
        conn.close()

    def load_students(self):

        conn = sqlite3.connect('attendance.db')
        c = conn.cursor()
        result = c.execute("SELECT* FROM students")

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        conn.commit()
        conn.close()

    def add_student(self):
        # DB connector
        conn = sqlite3.connect('attendance.db')
        c = conn.cursor()

        # user input of student info to be added as rows in db
        id = self.lineEdit.text()
        fname = self.lineEdit_2.text()
        lname = self.lineEdit_3.text()
        year = str(self.comboBox_2.currentText())
        course = str(self.comboBox.currentText())
        student_info = [(id, fname, lname, year, course)]
        c.execute("INSERT INTO students VALUES (?,?,?,?,?)", student_info)

        # this code updates the table students in UI
        result = c.execute("SELECT* FROM students")

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))


class AttendanceWin(QtWidgets.QMainWindow, Ui_A):
    def __init__(self):
        super().__init__()
        conn = sqlite3.connect('attendance.db')
        c = conn.cursor()
        self.setupUi(self)
        self.show()
        self.load_attendance()
        self.home_btn()
        self.add_btn()
        self.confirm_btn()
        c.execute("SELECT* FROM activities ORDER BY activity_id ASC")
        act = c.fetchall()[-1][5]
        self.label_2.setText("{}".format(act))

        det_time = self.timeEdit.time()
        time = det_time.currentTime()
        self.timeEdit.setTime(time)

    def home_btn(self):
        self.pushButton_3.clicked.connect(self.home)

    def home(self):
        self.close()
        self.newWin = MainWin()
        self.newWin.show()

    def add_btn(self):
        self.pushButton_2.clicked.connect(self.add_student)

    def load_attendance(self):
        conn = sqlite3.connect('attendance.db')
        c = conn.cursor()

        result = c.execute("SELECT students.student_id, students.first_name, students.last_name, students.course_id, "
                           "students.year_level, attends.status, attends.attendance_time, attends.activity_id FROM "
                           "attends INNER JOIN students ON students.student_id = attends.student_id")
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def add_student(self):
        conn = sqlite3.connect('attendance.db')
        c = conn.cursor()
        id = self.lineEdit_3.text()
        fname = self.lineEdit_2.text()
        lnamme = self.lineEdit_4.text()
        year = str(self.comboBox.currentText())
        course = (self.comboBox_5.currentText())
        student_info = [(id, fname, lnamme, year, course)]
        with conn:
            print("pushed")
            c.executemany("INSERT INTO students VALUES(?,?,?,?,?)", student_info)
        conn.commit()
        conn.close()

    def confirm_btn(self):
        self.pushButton.clicked.connect(self.take_attendance)

    def take_attendance(self):
        conn = sqlite3.connect('attendance.db')
        c = conn.cursor()
        c.execute("SELECT* FROM activities ORDER BY activity_id ASC")
        act = c.fetchall()[-1][5]
        det_time = self.timeEdit.time()
        times = det_time.currentTime()
        time = times.toString()

        get_date = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        print(get_date)
        status = self.comboBox_4.currentText()
        student_id = self.lineEdit_8.text()
        activity_id = act
        print(activity_id)
        attends = [(get_date, time, status, student_id, activity_id)]
        print(attends)
        conn = sqlite3.connect('attendance.db')
        c = conn.cursor()
        with conn:
            c.executemany("INSERT INTO attends VALUES(?,?,?,?,?)", attends)
        print('recorded')

        conn.commit()
        c.close()

        conn = sqlite3.connect('attendance.db')
        c = conn.cursor()

        result = c.execute("SELECT attends.student_id, students.first_name, students.last_name, students.course_id, "
                           "students.year_level, attends.status, attends.attendance_time, attends.activity_id FROM "
                           "attends INNER JOIN students ON students.student_id = attends.student_id")

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        conn.commit()
        c.close()


class ActivityWin(QtWidgets.QMainWindow, Ui_act):
    def __init__(self):
        super().__init__()
        print("pass")
        self.setupUi(self)
        print("pass")
        self.show()
        print("pass")
        self.load_activities()
        print("pass")
        conn = sqlite3.connect('attendance.db')
        c = conn.cursor()
        print("pass")
        self.pushButton_2.clicked.connect(self.home)
        print("pass")
        self.pushButton_4.clicked.connect(self.add_student)
        print("pass")
        self.pushButton_3.clicked.connect(self.attendance)
        print("pass")
        self.add_btn()
        print("pass")
        c.execute("SELECT* FROM activities ORDER BY activity_id ASC")
        act = c.fetchall()[-1][5]
        self.label_2.setText("{}".format(act))
        print("pass")

    # this code loads the activities table and displays the said activities
    def load_activities(self):
        conn = sqlite3.connect('attendance.db')
        c = conn.cursor()

        result = c.execute("SELECT* FROM activities")
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def add_btn(self):
        self.pushButton.clicked.connect(self.add_act)

    def add_act(self):
        conn = sqlite3.connect('attendance.db')
        c = conn.cursor()
        name = self.lineEdit.text()
        description = self.plainTextEdit.toPlainText()
        self.get_date = self.dateEdit.date()
        start_date = self.get_date.toString()
        get_endDate = self.dateEdit_2.date()
        end_date = get_endDate.toString()
        locations = self.lineEdit_2.text()
        c.execute("SELECT* FROM activities ORDER BY activity_id ASC")
        act = c.fetchall()[-1][5]
        activ = act + 1
        print(activ)

        activit = [(name, description, start_date, end_date, locations, activ)]
        print(activit)

        conn = sqlite3.connect('attendance.db')
        c = conn.cursor()
        with conn:
            c.executemany("INSERT INTO activities VALUES(?,?,?,?,?,?)", activit)
        conn.commit()
        conn.close()
        result = c.execute("SELECT* FROM activities")
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def add_student(self):
        self.close()
        self.studWin = studentWin()
        self.studWin.show()

    def attendance(self):
        self.close()
        self.newWin = AttendanceWin()
        self.newWin.show()

    def home(self):
        self.close()
        self.newWin = MainWin()
        self.newWin.show()

    def main(self):
        self.close()
        self.newWin = MainWin()
        self.newWin.show()


app = QtWidgets.QApplication(sys.argv)
win = MainWin()
win.show()
sys.exit(app.exec())
