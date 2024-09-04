import pandas as pd


class Student:
    def __init__(self, first_name, last_name, student_id, grade, teacher):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.grade = grade
        self.teacher = teacher

    def to_dict(self):
        return {
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "Student ID": self.student_id,
            "Grade": self.grade,
            "Teacher": self.teacher
        }

    @staticmethod
    def save_to_file(students, filename="data/students.csv"):
        data = [student.to_dict() for student in students]
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)

    @staticmethod
    def load_from_file(filename="data/students.csv"):
        df = pd.read_csv(filename)
        students = []
        for _, row in df.iterrows():
            students.append(
                Student(row['First Name'], row['Last Name'], row['Student ID'], row['Grade'], row['Teacher']))
        return students
