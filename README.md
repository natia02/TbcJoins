# University Database Management System

This project is a simple database management system for a university, built using Python and SQLite3. It allows you to manage advisors, students, and the advisor-student relationships.

## Features

- Create, read and update advisors and students
- Assign multiple advisors to a student and vice versa
- Generate reports showing the number of students per advisor and the number of advisors per student

## Prerequisites

- Python 3.x
- SQLite3

## Usage

- Create and Populate the database with sample data:

    ```bash
    python main.py
    ```

    This will read the `data.json` file and insert the advisors, students, and their relationships into the database.

- View the reports:

    ```bash
    python main.py
    ```

    This will display the following reports:

    - Advisors with the number of students they advise
    - Students with the number of advisors they have

## Files

- `advisor.py`: Contains the Advisor class for managing advisor data.
    - `get(advisor_id)`: Retrieves an advisor object from the database based on the advisor's ID.
    - `get_list(**kwargs)`: Retrieves a list of advisor objects from the database based on the provided keyword arguments (e.g., name, surname, age).
    - `update()`: Updates an existing advisor record in the database with the current attribute values.
    - `create()`: Inserts a new advisor record into the database with the current attribute values.
    - `save()`: Checks if an advisor record already exists in the database based on the advisor's name, surname, and age. If it exists, it updates the record; otherwise, it creates a new record.

- `student.py`: Contains the Student class for managing student data.
    - `get(student_id)`: Retrieves a student object from the database based on the student's ID.
    - `get_list(**kwargs)`: Retrieves a list of student objects from the database based on the provided keyword arguments (e.g., name, surname, age, gpa).
    - `update()`: Updates an existing student record in the database with the current attribute values.
    - `create()`: Inserts a new student record into the database with the current attribute values.
    - `save()`: Checks if a student record already exists in the database based on the student's name, surname, age, and GPA. If it exists, it updates the record; otherwise, it creates a new record.

- `studentAdvisor.py`: Contains the StudentAdvisor class for managing the advisor-student relationships.
    - `save()`: Inserts a new advisor-student relationship record into the database with the provided advisor ID and student ID.

- `db.py`: Creates the SQLite database and tables.
- `main.py`: Contains the main execution logic and report generation.
- `data.json`: Sample data file containing advisors and their students.
