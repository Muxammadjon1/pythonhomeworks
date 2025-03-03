import json
import csv

# Load tasks from tasks.json
def load_tasks(filename="tasks.json"):
    with open(filename, "r") as file:
        return json.load(file)

# Display tasks
def display_tasks(tasks):
    print("\nTask List:")
    print(f"{'ID':<5} {'Task Name':<20} {'Completed':<10} {'Priority':<8}")
    print("-" * 50)
    for task in tasks:
        print(f"{task['id']:<5} {task['task']:<20} {str(task['completed']):<10} {task['priority']:<8}")

# Save changes back to tasks.json
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

# Calculate task completion statistics
def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task["priority"] for task in tasks) / total_tasks

    print("\nTask Completion Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {avg_priority:.2f}")

# Convert tasks.json to tasks.csv
def convert_to_csv(tasks, filename="tasks.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task Name", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])
    print("\nTasks saved to tasks.csv.")

# Main Execution
tasks = load_tasks()
display_tasks(tasks)
calculate_stats(tasks)

# Modify a task (example: mark "Do laundry" as completed)
tasks[0]["completed"] = True
save_tasks(tasks)

# Convert to CSV
convert_to_csv(tasks)