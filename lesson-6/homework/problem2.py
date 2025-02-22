import os

# File name for storing employee records
FILE_NAME = "employees.txt"

# Function to add a new employee record
def add_employee():
    with open(FILE_NAME, "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
        print("Employee record added successfully!\n")

# Function to view all employee records
def view_employees():
    if not os.path.exists(FILE_NAME):
        print("No employee records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        records = file.readlines()
        if not records:
            print("No employee records found.\n")
            return
        
        print("Employee Records:")
        for record in records:
            print(record.strip())
        print()

# Function to search for an employee by Employee ID
def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False

    with open(FILE_NAME, "r") as file:
        for record in file:
            if record.startswith(emp_id + ","):
                print("Employee Found:", record.strip(), "\n")
                found = True
                break
    
    if not found:
        print("Employee not found.\n")

# Function to update an employee's information
def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    updated_records = []
    found = False

    with open(FILE_NAME, "r") as file:
        records = file.readlines()

    with open(FILE_NAME, "w") as file:
        for record in records:
            if record.startswith(emp_id + ","):
                found = True
                name = input("Enter new Name (or press Enter to keep unchanged): ") or record.split(",")[1].strip()
                position = input("Enter new Position (or press Enter to keep unchanged): ") or record.split(",")[2].strip()
                salary = input("Enter new Salary (or press Enter to keep unchanged): ") or record.split(",")[3].strip()

                updated_record = f"{emp_id}, {name}, {position}, {salary}\n"
                file.write(updated_record)
                print("Employee record updated successfully!\n")
            else:
                file.write(record)

    if not found:
        print("Employee ID not found.\n")

# Function to delete an employee record
def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    found = False

    with open(FILE_NAME, "r") as file:
        records = file.readlines()

    with open(FILE_NAME, "w") as file:
        for record in records:
            if record.startswith(emp_id + ","):
                found = True
                print("Employee record deleted successfully!\n")
            else:
                file.write(record)

    if not found:
        print("Employee ID not found.\n")

# Function to display the menu
def menu():
    while True:
        print("Employee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
menu()