import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"

    @staticmethod
    def add_employee():
        employee_id = input("Enter Employee ID: ")
        if EmployeeManager.search_employee(employee_id, display=False):
            print("Employee ID already exists. Try again.")
            return
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        
        with open(EmployeeManager.FILE_NAME, "a") as file:
            file.write(f"{employee_id},{name},{position},{salary}\n")
        print("Employee added successfully!")

    @staticmethod
    def view_all_employees():
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        
        with open(EmployeeManager.FILE_NAME, "r") as file:
            records = file.readlines()
        
        if not records:
            print("No employee records found.")
        else:
            print("Employee Records:")
            for record in records:
                print(record.strip())

    @staticmethod
    def search_employee(employee_id, display=True):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            return None
        
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(employee_id + ","):
                    if display:
                        print("Employee Found:")
                        print(line.strip())
                    return line.strip()
        
        if display:
            print("Employee not found.")
        return None

    @staticmethod
    def update_employee():
        employee_id = input("Enter Employee ID to update: ")
        records = []
        found = False
        
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        
        with open(EmployeeManager.FILE_NAME, "r") as file:
            records = file.readlines()
        
        with open(EmployeeManager.FILE_NAME, "w") as file:
            for record in records:
                if record.startswith(employee_id + ","):
                    found = True
                    name = input("Enter New Name: ")
                    position = input("Enter New Position: ")
                    salary = input("Enter New Salary: ")
                    file.write(f"{employee_id},{name},{position},{salary}\n")
                else:
                    file.write(record)
        
        if found:
            print("Employee record updated successfully!")
        else:
            print("Employee ID not found.")
    
    @staticmethod
    def delete_employee():
        employee_id = input("Enter Employee ID to delete: ")
        records = []
        found = False
        
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        
        with open(EmployeeManager.FILE_NAME, "r") as file:
            records = file.readlines()
        
        with open(EmployeeManager.FILE_NAME, "w") as file:
            for record in records:
                if not record.startswith(employee_id + ","):
                    file.write(record)
                else:
                    found = True
        
        if found:
            print("Employee record deleted successfully!")
        else:
            print("Employee ID not found.")

    @staticmethod
    def menu():
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                EmployeeManager.add_employee()
            elif choice == "2":
                EmployeeManager.view_all_employees()
            elif choice == "3":
                emp_id = input("Enter Employee ID to search: ")
                EmployeeManager.search_employee(emp_id)
            elif choice == "4":
                EmployeeManager.update_employee()
            elif choice == "5":
                EmployeeManager.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    EmployeeManager.menu()