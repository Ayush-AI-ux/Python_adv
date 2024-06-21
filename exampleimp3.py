class EmployeeDatabase:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, age, gender, position, salary):
        self.employees[emp_id] = {
            'name': name,
            'age': age,
            'gender': gender,
            'position': position,
            'salary': salary
        }

    def retrieve_employee_info(self, emp_id):
        employee = self.employees.get(emp_id)
        if employee:
            print("Employee Information:")
            print(f"Employee ID: {emp_id}")
            print(f"Name: {employee['name']}")
            print(f"Age: {employee['age']}")
            print(f"Gender: {employee['gender']}")
            print(f"Position: {employee['position']}")
            print(f"Salary: ${employee['salary']}")
        else:
            print("Employee not found in the database.")

    def update_salary(self, emp_id, new_salary):
        employee = self.employees.get(emp_id)
        if employee:
            employee['salary'] = new_salary
            print("Salary updated successfully.")
        else:
            print("Employee not found in the database.")

    def display_all_employees(self):
        if not self.employees:
            print("No employees in the database.")
            return

        print("All Employees:")
        for emp_id, employee in self.employees.items():
            print(f"Employee ID: {emp_id}, Name: {employee['name']}")

# Creating an instance of the EmployeeDatabase
employee_db = EmployeeDatabase()

while True:
    print("\n1. Add new employee")
    print("2. Retrieve employee information")
    print("3. Update salary")
    print("4. Display information of all employees")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        age = input("Enter employee age: ")
        gender = input("Enter employee gender: ")
        position = input("Enter employee position: ")
        salary = float(input("Enter employee salary: "))
        employee_db.add_employee(emp_id, name, age, gender, position, salary)
        print("Employee added successfully.")

    elif choice == '2':
        emp_id = input("Enter employee ID: ")
        employee_db.retrieve_employee_info(emp_id)

    elif choice == '3':
        emp_id = input("Enter employee ID: ")
        new_salary = float(input("Enter new salary: "))
        employee_db.update_salary(emp_id, new_salary)

    elif choice == '4':
        employee_db.display_all_employees()

    elif choice == '5':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
