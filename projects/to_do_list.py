class Task:
    """Represents a task with a description and status."""
    def __init__(self, description):
        """Constructor for the Task class."""
        self.description = description
        self.status = "Pending"

    def __str__(self):
        """Returns a string representation of the task."""
        return f"{self.description} - {self.status}"

    def mark_as_completed(self):
        """Marks the task as completed."""
        self.status = "Completed"

class TodoList:
    """Represents a list of tasks."""
    def __init__(self):
        """Constructor for the TodoList class."""
        self.tasks = []

    def add_task(self, task):
        """Adds a task to the list."""
        self.tasks.append(task)
        print(f"Task '{task.description}' added.")

    def remove_task(self, index):
        """Removes a task from the list by index."""
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task.description}' removed.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        """Displays all tasks in the list."""
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Current Tasks:")
            for i, task in enumerate(self.tasks):
                print(f"{i}. {task}")  # Uses the __str__ method of Task

    def get_task(self, index):
        """Gets a task from the list by index."""
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        else:
            return None

    def save_tasks(self, filename="tasks.txt"):
        """Saves tasks to a file."""
        try:
            with open(filename, "w") as f:
                for task in self.tasks:
                    f.write(f"{task.description},{task.status}\n")
            print(f"Tasks saved to {filename}")
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self, filename="tasks.txt"):
        """Loads tasks from a file."""
        try:
            with open(filename, "r") as f:
                self.tasks = []  # Clear existing tasks
                for line in f:
                    description, status = line.strip().split(",")
                    task = Task(description)
                    task.status = status
                    self.tasks.append(task)
            print(f"Tasks loaded from {filename}")
        except FileNotFoundError:
            print(f"File not found: {filename}.  Starting with an empty task list.")
        except Exception as e:
            print(f"Error loading tasks: {e}")

# Example Usage
todo = TodoList()
todo.load_tasks() #load the tasks

todo.add_task(Task("Learn Python"))
todo.add_task(Task("Build a project"))
todo.add_task(Task("Write documentation"))
todo.display_tasks()

task1 = todo.get_task(0)
if task1:
    task1.mark_as_completed()
todo.display_tasks()

todo.remove_task(1)
todo.display_tasks()

todo.save_tasks() #save the tasks


