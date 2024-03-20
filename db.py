import sqlite3


conn = sqlite3.connect('university.db')
conn.row_factory = sqlite3.Row
conn.execute("PRAGMA foreign_keys = ON")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS Student(
    student_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    age INTEGER NOT NULL,
    gpa REAL NOT NULL
)""")

c.execute("""
CREATE TABLE IF NOT EXISTS Advisor(
    advisor_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    age INTEGER NOT NULL
)""")

c.execute("""
CREATE TABLE IF NOT EXISTS StudentAdvisor(
    advisor_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    PRIMARY KEY(student_id, advisor_id),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (advisor_id) REFERENCES Advisor(advisor_id)
)""")


