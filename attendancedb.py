import sqlite3


def attendancedb():
    # initiate or connects data base

    connect = sqlite3.connect('attendance.db')
    cursor = connect.cursor()

    # creates table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS course(
        course_id VARCHAR(50) NOT NULL,
        course_name VARCHAR(50) NOT NULL,
        PRIMARY KEY(course_id)
            );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
        student_id	 VARCHAR(50) NOT NULL,
        first_name   VARCHAR(100) NOT NULL,
        last_name    VARCHAR(100) NOT NULL,
        year_level   VARCHAR(25) NOT NULL,
        course_id    INTEGER NOT NULL,
        PRIMARY KEY(student_id),
        FOREIGN KEY(course_id) REFERENCES course(course_id)
            );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attends(
        attendance_date	TEXT	NOT NULL,
        attendance_time	TEXT	NOT NULL,
        attendance_id	INTEGER	NOT NULL,
        status		VARCHAR(50)	NOT NULL,
        student_id  INTEGER NOT NULL,
        activity_id INTEGER NOT NULL,
        PRIMARY KEY(attendance_id),
        FOREIGN KEY(student_id)	REFERENCES students(student_id),
        FOREIGN KEY(activity_id)	REFERENCES activities(activity_id)
            );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS activities(
        activity_name	VARCHAR(50)	NOT NULL,
        activity_description	VARCHAR(500)	NOT NULL,
        start_date		TEXT			NOT NULL,
        end_date		TEXT			NOT NULL,
        location		VARCHAR(100)	NOT NULL,
        activity_id		INTEGER		NOT NULL,
        PRIMARY KEY(activity_id)
            );	

    """)

    connect.close()
    return 0


many_attends = [('2021-27-06', '08:30:15', '1', 'P', '2019-0001', '4'),
                ('2021-27-06', '08:32:10', '2', 'P', '2019-0002', '4'),
                ('2021-27-06', '08:33:45', '3', 'P', '2019-0003', '4')]
many_students = [('2019-0001', 'Student 1', 'Subject', '1st year', 'BSCS'),
                 ('2019-0002', 'Student 2', 'Database', '2nd year', 'BSIT'),
                 ('2019-0003', 'Student 3', 'Coding', '2nd year', 'BSCS'),
                 ('2019-0004', 'Student 4', 'Python', '3rd year', 'BSCA'),
                 ('2019-0005', 'Student 5', 'Pycharm', '2nd year', 'BSIS')]

many_activities = [('Seminar', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
                               'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, '
                               'quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo '
                               'consequat. ', '2019-26-09', '2019-26-09', 'Amphitheater', '0001'),
                   ('Palakasan', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
                                 'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, '
                                 'quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo '
                                 'consequat. ', '2020-26-03', '2020-28-03', 'Amphitheater', '0002'),
                   ('CCS days', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
                                'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, '
                                'quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo '
                                'consequat. ', '2020-25-04', '2020-25-04', 'Amphitheater', '0003'),
                   ('Sample Act', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
                                  'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, '
                                  'quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo '
                                  'consequat. ', '2021-27-06','2021-27-06','CCS 2nd floor','0004')]
many_course = [('BSCS', 'Bachelor of Computer Science'),
               ('BSIS', 'Bachelor of Information Studies'),
               ('BSCA', 'Bachelor of Computer Applications'),
               ('BSIT', 'Bachelor of Information technology')]

# connects the database
connect = sqlite3.connect('attendance.db')
cursor = connect.cursor()


# this function adds students using sqlite coding
def add_stud():
    cursor.executemany("INSERT INTO students VALUES (?,?,?,?,?)", many_students)
    cursor.execute("SELECT* FROM students")
    print(cursor.fetchall())


# this adds to the activities table
def add_act():
    cursor.executemany("INSERT INTO activities VALUES (?,?,?,?,?,?)", many_activities)
    cursor.execute("SELECT* FROM activities")
    print(cursor.fetchall())


# this adds to the course table
def add_course():
    cursor.executemany("INSERT INTO course VALUES (?,?)", many_course)
    cursor.execute("SELECT* FROM course")
    print(cursor.fetchall())


def add_attends():
    cursor.executemany("INSERT INTO attends VALUES(?,?,?,?,?,?)", many_attends)

'''
add_act()
add_stud()
add_course()
add_attends()'''
#cursor.execute("SELECT* FROM students")

print(cursor.fetchall())

connect.commit()
connect.close()
