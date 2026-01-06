class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks


class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self, roll, name, marks):
        self.students.append(Student(roll, name, marks))
        print("Student added successfully.")

    def display_students(self):
        if not self.students:
            print("No student records found.")
            return
        for s in self.students:
            print(f"Roll: {s.roll}, Name: {s.name}, Marks: {s.marks}")

    def search_student(self, roll):
        for s in self.students:
            if s.roll == roll:
                print(f"Found: {s.name}, Marks: {s.marks}")
                return
        print("Student not found.")


system = StudentManagement()

while True:
    print("\n1. Add Student\n2. Display Students\n3. Search Student\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        system.add_student(roll, name, marks)

    elif choice == "2":
        system.display_students()

    elif choice == "3":
        roll = int(input("Enter roll number to search: "))
        system.search_student(roll)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
