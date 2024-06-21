def admit_student(student_list):
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    student_details = {
        "Student ID": student_id,
        "Name": name,
        "Age": age,
        "Course": course
    }

    student_list.append(student_details)
    print("Student admitted successfully!\n")


def display_student_list(student_list):
    if not student_list:
        print("Student list is empty.\n")
    else:
        print("Admitted Student List:")
        for student in student_list:
            print("\n".join(f"{key}: {value}" for key, value in student.items()))
            print("-" * 20)
        print()


def update_student_information(student_list):
    student_id = input("Enter Student ID to update information: ")
    for student in student_list:
        if student["Student ID"] == student_id:
            field = input("Enter field to update (Name, Age, or Course): ").capitalize()
            new_value = input(f"Enter new {field}: ")
            student[field] = new_value
            print(f"{field} updated successfully!\n")
            return
    print("Student not found in the list.\n")


def search_student_by_id(student_list):
    student_id = input("Enter Student ID to search: ")
    for student in student_list:
        if student["Student ID"] == student_id:
            print("\n".join(f"{key}: {value}" for key, value in student.items()))
            print()
            return
    print("Student not found in the list.\n")


def calculate_average_age(student_list):
    if not student_list:
        print("Student list is empty.\n")
    else:
        total_age = sum(student["Age"] for student in student_list)
        average_age = total_age / len(student_list)
        print(f"Average Age of Admitted Students: {average_age:.2f}\n")


def remove_student_by_id(student_list):
    student_id = input("Enter Student ID to remove: ")
    for student in student_list:
        if student["Student ID"] == student_id:
            student_list.remove(student)
            print("Student removed successfully!\n")
            return
    print("Student not found in the list.\n")


def main():
    student_list = []

    while True:
        print("Student Admission Process Management System")
        print("1. Admit Student")
        print("2. Display Student List")
        print("3. Update Student Information")
        print("4. Search Student by ID")
        print("5. Calculate Average Age")
        print("6. Remove Student by ID")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            admit_student(student_list)
        elif choice == "2":
            display_student_list(student_list)
        elif choice == "3":
            update_student_information(student_list)
        elif choice == "4":
            search_student_by_id(student_list)
        elif choice == "5":
            calculate_average_age(student_list)
        elif choice == "6":
            remove_student_by_id(student_list)
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.\n")

