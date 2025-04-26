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
                    task = Store_Task(parts[0], parts[1], parts[2])
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
    task = Store_Task(task_id, title, description)
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

def delete_task():
    task_id = input("Enter Task ID to Delete: ")
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            save_tasks()
            print("Task deleted!")
            return
    print("Task not found!")

def menu():
    load_tasks()

    while True:
        print("\n---- Task Manager ----")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Tasks")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("choose an option 1 ot 5: ")

        if choice == '1':
            create_task()
        elif choice == '2':
            read_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting Task Manager....")
            break
        else:
            print("Invalid option! Try again.")

menu()