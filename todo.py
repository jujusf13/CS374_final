# Patrick --> Task to ToDoList

class Task:
    PRIORITY_MAP = {"LOW": 1, "MEDIUM": 2, "HIGH": 3}  # Lower number = higher priority

    def __init__(self, description, priority):
        self.task = task
        self.priority = priority.upper()  # Always uppercase

    # less than magic method. Assigns a number to each tasks (1 for low, 2 for medium, 3 for high) to later compare
    def __lt__(self, other):
        inOrder = Task.PRIORITY_MAP[self.priority] < Task.PRIORITY_MAP[other.priority]
        return inOrder

    # so we return a string and not a space in memory
    def __str__(self):
        return f"{self.description} (Priority: {self.priority})"
        

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority="MEDIUM"):
        self.tasks.append(Task(description, priority))
        return "Task added successfully."

    #removes task and prints name of task
    def remove_task(self, index):
        if index < 1 or index > len(self.tasks):
            return "Invalid task number."
        removed = self.tasks.pop(index - 1)
        return f"Removed task: {removed}"

    # loops through tasks
    def show_all(self):
        if not self.tasks:
            return "No tasks to show."
        result = "Tasks:\n"
        for i, task in enumerate(self.tasks, start=1):
            result += f"{i}. {task}\n"
        return result

    # Sorts items by checking value of each task (1, 2, or 3)
    def show_by_priority(self):
        if not self.tasks:
            return "No tasks to show."
        sorted_tasks = sorted(self.tasks) # Uses __lt__ here. Error without that piece of code.
        # takes in an array^^^^^ and sorts it
        result = "Tasks sorted by priority:\n"
        for i, task in enumerate(sorted_tasks, start=1):
            result += f"{i}. {task}\n"
        return result

# Pat McManus --> Parse_command code
def parse_command(command, todo_list):
    parts = command.split()
    try:
        if parts[0] == "ADD":
            task_start = command.index('"') + 1
            task_end = command.index('"', task_start)
            description = command[task_start:task_end]
            priority = "MEDIUM"
            if "PRIORITY" in parts:
                priority_index = parts.index("PRIORITY") + 1
                priority = parts[priority_index]
            return todo_list.add_task(description, priority)
        elif parts[0] == "REMOVE":
            index = int(parts[1])
            return todo_list.remove_task(index)
        elif parts[0] == "SHOW":
            if parts[1] == "ALL":
                return todo_list.show_all()
            elif parts[1] == "BY" and parts[2] == "PRIORITY":
                return todo_list.show_by_priority()
            else:
                return "Invalid SHOW command."
        else:
            return "Unknown command."
    except (ValueError, IndexError):
        return "Invalid command format."
