import json


def save_tasks(tasks_list):
    data_to_save = []
    for task in tasks_list:
        # Convert the task object to a simple dictionary
        task_dict = {
            "title": task.title,
            "description": task.description,
            "sessions": task.sessions,
            "is_completed": task.is_completed
        }
        data_to_save.append(task_dict)

    # Write to a file called 'tasks.json'
    with open("tasks.json", "w") as f:
        # YOUR CODE HERE to dump the data
        json.dump(data_to_save, f, indent=4)
        print("Data saved successfully!")


def load_tasks():
    # Check if the file exists first so the program doesn't crash
    if not os.path.exists('tasks.json'):
        return []

    with open('tasks.json', "r") as f:
        data = json.load(f)

    loaded_tasks = []
    for item in data:
        # Create a new Task object from the saved data
        task = Task(item['title'], item['description'])
        task.sessions = item['sessions']
        task.is_completed = item['is_completed']
        loaded_tasks.append(task)

    return loaded_tasks