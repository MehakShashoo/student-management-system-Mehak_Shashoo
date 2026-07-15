class Student:
    total_students = 0

    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        Student.total_students += 1

    def get_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        return "Fail"

    def display(self):
        print("-" * 30)
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"Marks   : {self.marks}")
        print(f"Grade   : {self.get_grade()}")
        print("-" * 30)

    @classmethod
    def show_total_students(cls):
        print(f"Total Students : {cls.total_students}")

    @staticmethod
    def valid_marks(marks):
        return 0 <= marks <= 100