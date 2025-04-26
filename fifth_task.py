class Store_Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id 
        self.title = title
        self.description = description
    
    def __str__(self):
        return f"{self.task_id},{self.title},{self.description}"
    

tasks = []
file_name = "tasks.txt"

def load_tasks():
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    task = Task(parts[0], parts[1], parts[2])
                    task.append(task)
    except FileNotFoundError:
        pass

def save_tasks():
    with open(file_name,'w')as file:
        for task in tasks:
            file.write(str(task) + "\n")

def create_task():
    task_id = input("enter task Id: ")
    title = input("enter task title: ")
    description = input("enter task description: ")
    task = Task(task_id, title, description)
    tasks.append(task)
    save_tasks()
    print("Task added!")

def read_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for task in task:
            print(f"ID: {task.task_id} | Title: {task.title} | Description: {task.description}")

def update_task():
    task_id = input("Enter Task ID to update: ")
    for task in tasks:
        if task.task_id == task_id:
            task.title = input("Enter new title: ")
            task.description = input("Enter new Description: ")
            save_tasks()
            print("Task updated!")
            return
    print("Task not found!")
