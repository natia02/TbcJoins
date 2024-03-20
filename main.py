from db import c, conn
import json
from advisor import Advisor
from student import Student
from studentAdvisor import StudentAdvisor


def fill_tables(info):
    for advisor_data in info["advisors"]:
        advisor = Advisor(advisor_data['name'], advisor_data['surname'], advisor_data['age'])
        advisor.save()

        for student_data in advisor_data['students']:
            student = Student(student_data['name'], student_data['surname'], student_data['age'], student_data['gpa'])
            student.save()

            student_advisor = StudentAdvisor(advisor.advisor_id, student.student_id)
            student_advisor.save()


def advisors_with_number_of_students():
    result = c.execute("""
    SELECT a.advisor_id, a.name, COUNT(s.student_id) AS number_of_students 
    FROM Student s INNER JOIN StudentAdvisor sa on sa.student_id = s.student_id
    INNER JOIN Advisor a ON sa.advisor_id = a.advisor_id
    GROUP BY a.advisor_id
    ORDER BY number_of_students
    """)

    print("Advisor ID\t\tName\t\t\tNumber of Students")
    print("-----------------------------------------------")
    for row in result.fetchall():
        print(f"{row['advisor_id']:<12}\t{row['name']:<20}\t{row['number_of_students']}")


def students_with_number_of_advisors():
    result = c.execute("""
    SELECT s.student_id, s.name, COUNT(a.advisor_id) AS number_of_advisors
    FROM Student s INNER JOIN StudentAdvisor sa on sa.student_id = s.student_id
    INNER JOIN Advisor a ON sa.advisor_id = a.advisor_id
    GROUP BY s.student_id
    ORDER BY number_of_advisors
    """)

    print("\nStudent ID\t\tName\t\t\tNumber of Advisors")
    print("-----------------------------------------")
    for row in result.fetchall():
        print(f"{row['student_id']:<12}\t{row['name']:<20}\t{row['number_of_advisors']}")


if __name__ == '__main__':
    if Advisor.is_empty() or StudentAdvisor.is_empty() or Student.is_empty():
        with open('data.json', 'r') as file:
            data = json.load(file)
        fill_tables(data)

    advisors_with_number_of_students()
    students_with_number_of_advisors()


