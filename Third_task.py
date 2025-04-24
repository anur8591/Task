# Simple CRUD Task Manager - Beginner Version

class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description

    def __str__(self):
        return f"ID: {self.task_id}, Title: {self.title}, Description: {self.description}"

# List to store tasks
tasks = []

# Create task
def create_task():
    task_id = input("Enter Task ID: ")
    title = input("Enter Task Title: ")
    description = input("Enter Task Description: ")
    task = Task(task_id, title, description)
    tasks.append(task)
    print("✅ Task added!")

# Read tasks
def read_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(task)

# Update task
def update_task():
    task_id = input("Enter Task ID to update: ")
    for task in tasks:
        if task.task_id == task_id:
            task.title = input("Enter new title: ")
            task.description = input("Enter new description: ")
            print("✅ Task updated!")
            return
    print("❌ Task not found!")

