def add_medicine(inventory):
    medicine_id = input("Enter Medicine ID: ")
    medicine_name = input("Enter Medicine Name: ")
    quantity = int(input("Enter Quantity: "))
    price = int(input("Enter Price: "))

    medicine_details = {
        "Medicine ID": medicine_id,
        "Medicine Name": medicine_name,
        "Quantity": quantity,
        "Price": price
    }

    inventory.append(medicine_details)
    print("Medicine added successfully!\n")


def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty.\n")
    else:
        print("Medicine Inventory:")
        for medicine in inventory:
            print("\n".join(f"{key}: {value}" for key, value in medicine.items()))
            print("-" * 20)
        print()


def update_quantity(inventory):
    medicine_id = input("Enter Medicine ID to update quantity: ")
    for medicine in inventory:
        if medicine["Medicine ID"] == medicine_id:
            new_quantity = int(input("Enter new quantity: "))
            medicine["Quantity"] = new_quantity
            print("Quantity updated successfully!\n")
            return
    print("Medicine not found in inventory.\n")


def search_by_id(inventory):
    medicine_id = input("Enter Medicine ID to search: ")
    for medicine in inventory:
        if medicine["Medicine ID"] == medicine_id:
            print("\n".join(f"{key}: {value}" for key, value in medicine.items()))
            print()
            return
    print("Medicine not found in inventory.\n")


def main():
    medicine_inventory = []

    while True:
        print("Medicine Store Management System")
        print("1. Add Medicine")
        print("2. Display Medicine Inventory")
        print("3. Update Medicine Quantity")
        print("4. Search Medicine by ID")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_medicine(medicine_inventory)
        elif choice == "2":
            display_inventory(medicine_inventory)
        elif choice == "3":
            update_quantity(medicine_inventory)
        elif choice == "4":
            search_by_id(medicine_inventory)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")

