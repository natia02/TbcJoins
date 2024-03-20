from db import c, conn


class StudentAdvisor:
    def __init__(self, advisor_id, student_id):
        self.advisor_id = advisor_id
        self.student_id = student_id

    def __str__(self):
        return f'Advisor: {self.advisor_id}, Student: {self.student_id}'

    def __eq__(self, other):
        if isinstance(other, StudentAdvisor):
            return (self.advisor_id == other.advisor_id
                    and self.student_id == other.student_id)
        return False

    def __repr__(self):
        return f"Advisor: {self.advisor_id}, Student: {self.student_id}"

    @classmethod
    def is_empty(cls):
        return c.execute("SELECT COUNT(*) FROM StudentAdvisor").fetchone()[0] == 0

    def save(self):
        c.execute("INSERT INTO StudentAdvisor (advisor_id, student_id) VALUES (?, ?)",
                  (self.advisor_id, self.student_id))
        conn.commit()
