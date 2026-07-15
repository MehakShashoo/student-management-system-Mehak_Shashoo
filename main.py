from student import Student
students = []
def find_student(roll_no):
    for student in students:
        if student.roll_no == roll_no:
            return student
    return None
def add_student():
    roll_no = int(input("Enter Roll Number : "))
    if find_student(roll_no):
        print("Roll Number already exists.")
        return
    name = input("Enter Name : ")
    marks = float(input("Enter Marks : "))
    if not Student.valid_marks(marks):
        print("Marks should be between 0 and 100.")
        return
    students.append(Student(roll_no, name, marks))
    print("Student Added Successfully.")
def view_students():
    if not students:
        print("No student records found.")
        return
    for student in students:
        student.display()
def search_student():
    roll_no = int(input("Enter Roll Number : "))

    student = find_student(roll_no)
    if student:
        student.display()
    else:
        print("Student Not Found")
def update_marks():
    roll_no = int(input("Enter Roll Number : "))
    student = find_student(roll_no)
    if student:
        marks = float(input("Enter New Marks : "))
        if not Student.valid_marks(marks):
            print("Invalid Marks")
            return
        student.marks = marks
        print("Marks Updated Successfully")
    else:
        print("Student Not Found")
def delete_student():
    roll_no = int(input("Enter Roll Number : "))
    student = find_student(roll_no)
    if student:
        students.remove(student)
        Student.total_students -= 1
        print("Student Deleted Successfully")
    else:
        print("Student Not Found")
def show_topper():
    if not students:
        print("No students available.")
        return
    topper = students[0]
    for student in students:
        if student.marks > topper.marks:
            topper = student
    print("\nTopper")
    topper.display()
def menu():
    while True:

        print("\n==============================")
        print(" Student Management System")
        print("==============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Show Topper")
        print("7. Exit")
        choice = input("Enter your choice : ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            show_topper()
        elif choice == "7":
            print("Thank You")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    menu()