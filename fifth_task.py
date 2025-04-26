class Store_Task:
    def __init__(self, task_id, title, discription):
        self.task_id = task_id 
        self.title = title
        self.discription = discription
    
    def __str__(self):
        return f"{self.task_id},{self.title},{self.discription}"