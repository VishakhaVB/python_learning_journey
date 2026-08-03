students = {}

def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks: "))

    students[roll_no] = {
        "Name": name,
        "Marks": marks
    }

    print("Student Record Added Successfully!\n")


def display_students():
    if not students:
        print("No Records Found!\n")
    else:
        print("\nStudent Records:")
        for roll, details in students.items():
            print(f"Roll No: {roll}")
            print(f"Name    : {details['Name']}")
            print(f"Marks   : {details['Marks']}")
            print("----------------------")


def search_student():
    roll_no = input("Enter Roll Number to Search: ")

    if roll_no in students:
        print("\nStudent Found:")
        print("Name  :", students[roll_no]["Name"])
        print("Marks :", students[roll_no]["Marks"])
    else:
        print("Student Record Not Found!")


def delete_student():
    roll_no = input("Enter Roll Number to Delete: ")

    if roll_no in students:
        del students[roll_no]
        print("Student Record Deleted Successfully!\n")
    else:
        print("Student Record Not Found!\n")


while True:
    print("\n===== Student Record Management =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()

    elif choice == '2':
        display_students()

    elif choice == '3':
        search_student()

    elif choice == '4':
        delete_student()

    elif choice == '5':
        print("Program Exited.")
        break

    else:
        print("Invalid Choice! Please try again.")
