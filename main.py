import sqlite3

db = sqlite3.connect('mydatabase.db')

school = db.cursor()

school.execute(
    'CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT,age INTEGER,grade TEXT);')

school.execute('INSERT INTO  students(name,age,grade)VALUES("axror",13,5+);')
db.commit()
school.execute('INSERT INTO  students(name,age,grade)VALUES("albert",16,5-);')
db.commit()
school.execute('INSERT INTO  students(name,age,grade)VALUES("fathulla",20,4+);')
db.commit()


def get_student_by_name(name, age, grade):
    db = sqlite3.connect('mydatabase.db')

    school = db.cursor()

    result = school.execute('SELECT name,phone_number FROM users WHERE name=? and age=? and grade=? ;', (name
                                                                                                         ,
                                                                                                         age,
                                                                                                         grade)).fetchone()


db.commit()


def update_student_grade(name, grade):
    db = sqlite3.connect('mydatabase.db')

    school = db.cursor()

    new = school.execute('UPDATE students SET name=? and grade=? WHERE id?; ', (name, grade,)).fetchone()


db.commit()


def delete_student(name):
    db = sqlite3.connect('mydatabase.db')

    school = db.cursor()

    delete = school.execute('DELETE * FROM students WHERE name=?;', (name,))


db.commit()
