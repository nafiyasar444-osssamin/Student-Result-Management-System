import os

students = {}

# ---------- Load Data ----------
if os.path.exists("students.txt"):
    with open("students.txt", "r") as file:
        for line in file:
            name, marks = line.strip().split(",")
            students[name] = float(marks)


def save_data():
    with open("students.txt", "w") as file:
        for name, marks in students.items():
            file.write(f"{name},{marks}\n")


def grade(mark):
    if mark >= 80:
        return "A+"
    elif mark >= 70:
        return "A"
    elif mark >= 60:
        return "A-"
    elif mark >= 50:
        return "B"
    elif mark >= 40:
        return "C"
    else:
        return "F"


while True:

    print("\n===== Student Result System =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Student Name: ")
        marks = float(input("Marks: "))

        students[name] = marks

        save_data()

        print("Student Added Successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("No Student Found")

        else:

            print("\nName\tMarks\tGrade")

            for name, marks in students.items():
                print(name, "\t", marks, "\t", grade(marks))

    elif choice == "3":

        name = input("Enter Student Name: ")

        if name in students:

            print("Marks:", students[name])
            print("Grade:", grade(students[name]))

        else:

            print("Student Not Found")

    elif choice == "4":

        name = input("Student Name: ")

        if name in students:

            new_marks = float(input("New Marks: "))

            students[name] = new_marks

            save_data()

            print("Updated Successfully")

        else:

            print("Student Not Found")

    elif choice == "5":

        name = input("Student Name: ")

        if name in students:

            del students[name]

            save_data()

            print("Deleted Successfully")

        else:

            print("Student Not Found")

    elif choice == "6":

        print("Thank You")

        break

    else:

        print("Invalid Choice")
