from db import c, conn


class Student:
    def __init__(self, name, surname, age, gpa, student_id=None):
        self.student_id = student_id
        self.name = name
        self.surname = surname
        self.age = age
        self.gpa = gpa

    def __str__(self):
        return f'ID: {self.student_id}, Name: {self.name}, Surname: {self.surname}'

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False

    @classmethod
    def is_empty(cls):
        return c.execute("SELECT COUNT(*) FROM Student").fetchone()[0] == 0

    @classmethod
    def get(cls, student_id):
        result = c.execute("SELECT * FROM Student WHERE student_id=?", (student_id,))
        values = result.fetchall()
        if values is None:
            return None
        student = Student(values["name"], values["surname"], values["age"], values["gpa"], student_id)
        return student

    @classmethod
    def get_list(cls, **kwargs):
        query = "SELECT DISTINCT * FROM Student WHERE "
        conditions = []
        values = []
        for key, value in kwargs.items():
            conditions.append(f"{key} = ?")
            values.append(value)
        query += " AND ".join(conditions)
        result = c.execute(query, tuple(values))

        students = []
        for row in result.fetchall():
            students.append(Student(row["name"], row["surname"], row["age"], row["gpa"]))
        return students

    def __repr__(self):
        return f"Student: {self.student_id}, {self.name}"

    def update(self):
        c.execute("UPDATE Student SET name = ?, surname = ?, age = ?, gpa = ? WHERE Student.student_id = ?",
                  (self.name, self.surname, self.age, self.gpa, self.student_id))
        conn.commit()

    def create(self):
        c.execute("INSERT INTO Student (name, surname, age, gpa) VALUES (?, ?, ?, ?)",
                  (self.name, self.surname, self.age, self.gpa))
        self.student_id = c.lastrowid
        conn.commit()

    def save(self):
        student = c.execute("""
        SELECT student_id 
        from Student 
        where name == ? and surname = ? and age = ? and gpa = ?""",
                            (self.name, self.surname, self.age, self.gpa)).fetchone()

        if student is not None:
            self.student_id = student["student_id"]

        if self.student_id is not None:
            self.update()
        else:
            self.create()
        return self
