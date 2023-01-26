import sqlite3 as sql


# This creates an sqlite file if it doesn't exist and opens it otherwise

def get_students(cursor):
    student_read = '''
            SELECT * FROM student;
            '''
    cursor.execute(student_read)
    return cursor.fetchall()


def get_subjects(cursor):
    subject_read = '''
            SELECT * FROM subjects;
            '''
    cursor.execute(subject_read)
    return cursor.fetchall()


def add_subject(cursor):
    ...


def get_house(cursor, pupil_id):
    house_read = '''
                SELECT firstname, lastname, year, house.name FROM house JOIN tutorgroup
                on house.ID = tutorgroup.HouseID
                join student on student.TutorGroupID = tutorgroup.ID
                where student.id = ?;
                '''
    cursor.execute(house_read, (pupil_id,))
    return cursor.fetchall()


with sql.connect('student.db') as conn:
    # The cursor is used to read and write to the database

    cursor = conn.cursor()

    # This will add a single entry to the student table

    # We then execute it using cursor

    all_students = get_students(cursor)

    for s in all_students:
        print(s)
    pupil_id = input("Enter a pupil id: ")
while True:

    choice = input("Options:\n"
                   "1: Print House\n"
                   "2: Get subject\n"
                   "3: Add subject\n")

    if choice == "1":
        print(get_house(cursor, pupil_id))
    if choice == "2":
        print(get_subjects(cursor))
