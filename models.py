class Task:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.sessions = [] 
        self.is_completed = False

    def add_session(self, duration: float):
        self.sessions.append(duration)

    def get_total_time(self):
        return sum(self.sessions)

    def __str__(self):
        status = "Done" if self.is_completed else "Pending"
        return f"[{status}] {self.title} - Total: {self.get_total_time()}s"


class TaskManager:
    def __init__(self):
        self.tasks = []


    def add_task(self, title, description):
        new_task = Task(title, description)
        self.tasks.append(new_task)

    def find_task(self, title: str):
        for task in self.tasks:
            if task.title == title:
                return task
        return None
