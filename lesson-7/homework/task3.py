import json
import csv
from abc import ABC, abstractmethod

# Task Class
class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "Task ID": self.task_id,
            "Title": self.title,
            "Description": self.description,
            "Due Date": self.due_date,
            "Status": self.status,
        }

# Abstract FileHandler
class FileHandler(ABC):
    @abstractmethod
    def load_tasks(self):
        pass

    @abstractmethod
    def save_tasks(self, tasks):
        pass

# CSV File Handler
class CSVHandler(FileHandler):
    def __init__(self, filename="tasks.csv"):
        self.filename = filename

    def load_tasks(self):
        tasks = []
        try:
            with open(self.filename, newline="", mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    tasks.append(Task(**row))
        except FileNotFoundError:
            pass
        return tasks

    def save_tasks(self, tasks):
        with open(self.filename, mode="w", newline="") as file:
            fieldnames = ["Task ID", "Title", "Description", "Due Date", "Status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

# JSON File Handler
class JSONHandler(FileHandler):
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Task(**task) for task in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self, tasks):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)

# To-Do Manager Class
class ToDoManager:
    def __init__(self, file_handler):
        self.file_handler = file_handler
        self.tasks = self.file_handler.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.file_handler.save_tasks(self.tasks)
        print("Task added successfully!")

    def view_tasks(self):
        for task in self.tasks:
            print(task.to_dict())

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title: task.title = title
                if description: task.description = description
                if due_date: task.due_date = due_date
                if status: task.status = status
                self.file_handler.save_tasks(self.tasks)
                print("Task updated!")
                return
        print("Task not found!")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.file_handler.save_tasks(self.tasks)
        print("Task deleted!")

    def filter_tasks(self, status):
        filtered = [task for task in self.tasks if task.status == status]
        for task in filtered:
            print(task.to_dict())

# Usage Example
if __name__ == "__main__":
    manager = ToDoManager(JSONHandler())  # Switch to CSVHandler() for CSV
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Filter Tasks\n6. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            task = Task(
                task_id=input("Task ID: "),
                title=input("Title: "),
                description=input("Description: "),
                due_date=input("Due Date: "),
                status=input("Status: ")
            )
            manager.add_task(task)
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            manager.update_task(
                task_id=input("Enter Task ID: "),
                title=input("New Title (leave blank if unchanged): ") or None,
                description=input("New Description (leave blank if unchanged): ") or None,
                due_date=input("New Due Date (leave blank if unchanged): ") or None,
                status=input("New Status (leave blank if unchanged): ") or None
            )
        elif choice == "4":
            manager.delete_task(input("Enter Task ID to delete: "))
        elif choice == "5":
            manager.filter_tasks(input("Enter Status to filter by: "))
        elif choice == "6":
            break
