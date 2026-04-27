# Smart Task & Time Manager

A robust, terminal-based productivity tool built with **Pure Python**. This project demonstrates advanced programming concepts including Object-Oriented Programming (OOP), Custom Decorators, and Data Persistence.

## 🚀 Key Features

* **OOP-Based Architecture**: Utilizes a `Task` and `TaskManager` class structure for clean, modular code.
* **Automatic Time Tracking**: Implements a **Custom Python Decorator** to measure and log the duration of work sessions automatically.
* **Data Persistence**: Uses **JSON serialization** to save your tasks and session history to a local file, ensuring data is kept between runs.
* **Clean CLI**: A user-friendly command-line interface for managing and viewing tasks.

## 🛠️ Technical Concepts Demonstrated

### 1. Object-Oriented Programming (OOP)
The project is built on the foundation of classes and objects. By using a `TaskManager`, the application logic is separated from the data, making it easy to scale and maintain.

### 2. Python Decorators
The `@track_time` decorator in `decorators.py` is used to wrap "work" functions. This shows an understanding of higher-order functions and how to modify behavior without changing the source code of the function.

### 3. File I/O & JSON
The `storage.py` module handles the transformation of complex Python objects into JSON format and back again (Serialization/Deserialization).

## 📂 Project Structure

- `main.py`: The entry point containing the user menu logic.
- `models.py`: Defines the `Task` and `TaskManager` blueprints.
- `decorators.py`: Contains the logic for the `@track_time` decorator.
- `storage.py`: Manages saving and loading data from `tasks.json`.

## 💻 How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/YourUsername/smart-task-manager.git](https://github.com/YourUsername/smart-task-manager.git)
