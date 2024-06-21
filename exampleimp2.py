class PatientDatabase:
    def __init__(self):
        self.patients = {}

    def add_patient(self, patient_id, name, age, gender, contact_number, medical_history):
        self.patients[patient_id] = {
            'name': name,
            'age': age,
            'gender': gender,
            'contact_number': contact_number,
            'medical_history': medical_history
        }

    def retrieve_patient_info(self, patient_id):
        patient = self.patients.get(patient_id)
        if patient:
            print("Patient Information:")
            print(f"Patient ID: {patient_id}")
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            print(f"Gender: {patient['gender']}")
            print(f"Contact Number: {patient['contact_number']}")
            print(f"Medical History: {', '.join(patient['medical_history'])}")
        else:
            print("Patient not found in the database.")

    def update_medical_history(self, patient_id, new_medical_history):
        patient = self.patients.get(patient_id)
        if patient:
            patient['medical_history'] = new_medical_history
            print("Medical history updated successfully.")
        else:
            print("Patient not found in the database.")

    def display_all_patients(self):
        if not self.patients:
            print("No patients in the database.")
            return

        print("All Patients:")
        for patient_id, patient in self.patients.items():
            print(f"Patient ID: {patient_id}, Name: {patient['name']}")

# Creating an instance of the PatientDatabase
patient_db = PatientDatabase()

while True:
    print("\n1. Add new patient")
    print("2. Retrieve patient information")
    print("3. Update medical history")
    print("4. Display information of all patients")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        patient_id = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        age = input("Enter patient age: ")
        gender = input("Enter patient gender: ")
        contact_number = input("Enter patient contact number: ")
        medical_history = input("Enter patient medical history (comma-separated): ").split(',')
        patient_db.add_patient(patient_id, name, age, gender, contact_number, medical_history)
        print("Patient added successfully.")

    elif choice == '2':
        patient_id = input("Enter patient ID: ")
        patient_db.retrieve_patient_info(patient_id)

    elif choice == '3':
        patient_id = input("Enter patient ID: ")
        new_medical_history = input("Enter new medical history (comma-separated): ").split(',')
        patient_db.update_medical_history(patient_id, new_medical_history)

    elif choice == '4':
        patient_db.display_all_patients()

    elif choice == '5':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
