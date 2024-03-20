from db import c, conn


class Advisor:
    def __init__(self, name, surname, age, advisor_id=None):
        self.advisor_id = advisor_id
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f'ID: {self.advisor_id}, Name: {self.name}, Surname: {self.surname}'

    def __eq__(self, other):
        if isinstance(other, Advisor):
            return self.advisor_id == other.advisor_id
        return False

    @classmethod
    def is_empty(cls):
        return c.execute("SELECT COUNT(*) FROM Advisor").fetchone()[0] == 0

    @classmethod
    def get(cls, advisor_id):
        result = c.execute("SELECT * FROM Advisor WHERE advisor_id = ?", (advisor_id,))
        values = result.fetchone()
        if values is None:
            return None
        advisor = Advisor(values["name"], values["surname"], values["age"], values["id"])
        return advisor

    @classmethod
    def get_list(cls, **kwargs):
        query = "SELECT DISTINCT * FROM Advisor WHERE "
        conditions = []
        values = []
        for key, value in kwargs.items():
            conditions.append(f"{key} = ?")
            values.append(value)
        query += " AND ".join(conditions)
        result = c.execute(query, tuple(values))

        advisors = []
        for row in result.fetchall():
            advisors.append(Advisor(row["name"], row["surname"], row["age"]))
        return advisors

    def __repr__(self):
        return f"Advisor: {self.advisor_id}, {self.name}"

    def update(self):
        c.execute("UPDATE Advisor SET name = ?, surname = ?, age = ? WHERE advisor_id = ?",
                  (self.name, self.surname, self.age, self.advisor_id))
        conn.commit()

    def create(self):
        c.execute("INSERT INTO Advisor (name, surname, age) VALUES (?, ?, ?)", (self.name, self.surname, self.age))
        self.advisor_id = c.lastrowid
        conn.commit()

    def save(self):
        advisor = c.execute("""
        SELECT advisor_id
        from Advisor
        where name == ? and surname = ? and age = ?""",
                            (self.name, self.surname, self.age)).fetchone()

        if advisor is not None:
            self.advisor_id = advisor["advisor_id"]

        if (self.advisor_id is not None) or (advisor is not None):
            self.update()
        else:
            self.create()
        return self
