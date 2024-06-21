def add_student(database, name, roll_number, marks):
    database[roll_number] = {'name': name, 'marks': marks}

def display_student_details(database, roll_number):
    student = database.get(roll_number)
    if student:
        print(f"Name: {student['name']}")
        print(f"Roll Number: {roll_number}")
        print(f"Marks: {student['marks']}")
    else:
        print("Student not found in the database.")

def display_average_marks(database):
    total_subjects = len(next(iter(database.values()))['marks'])
    total_students = len(database)
    
    if total_students == 0:
        print("No students in the database.")
        return
    
    total_marks = [sum(student['marks']) for student in database.values()]
    average_marks = [round(sum(marks) / total_subjects, 2) for marks in zip(*total_marks)]
    
    print(f"Average Marks: {average_marks}")

def display_percentage(database):
    total_subjects = len(next(iter(database.values()))['marks'])
    
    if not database:
        print("No students in the database.")
        return
    
    for roll_number, student in database.items():
        percentage = (sum(student['marks']) / (total_subjects * 100)) * 100
        print(f"Roll Number: {roll_number}, Percentage: {round(percentage, 2)}%")

def display_grade(database, roll_number):
    student = database.get(roll_number)
    
    if student:
        average_marks = sum(student['marks']) / len(student['marks'])
        if average_marks >= 90:
            grade = 'A'
        elif 80 <= average_marks < 90:
            grade = 'B'
        elif 70 <= average_marks < 80:
            grade = 'C'
        elif 60 <= average_marks < 70:
            grade = 'D'
        else:
            grade = 'F'
        
        print(f"Roll Number: {roll_number}, Grade: {grade}")
    else:
        print("Student not found in the database.")

# Sample database
student_database = {}

while True:
    print("\n1. Add new student")
    print("2. Display student details")
    print("3. Display average marks")
    print("4. Display percentage of all students")
    print("5. Display grade of a specific student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        marks = [float(input(f"Enter marks for Subject {i+1}: ")) for i in range(3)]
        add_student(student_database, name, roll_number, marks)
        print("Student added successfully.")

    elif choice == '2':
        roll_number = input("Enter roll number of the student: ")
        display_student_details(student_database, roll_number)

    elif choice == '3':
        display_average_marks(student_database)

    elif choice == '4':
        display_percentage(student_database)

    elif choice == '5':
        roll_number = input("Enter roll number of the student: ")
        display_grade(student_database, roll_number)

    elif choice == '6':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.") 