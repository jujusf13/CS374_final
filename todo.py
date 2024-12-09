class Task:
    PRIORITY_MAP = {"LOW": 1, "MEDIUM": 2, "HIGH": 3}  # Lower number = higher priority

    def __init__ (self, description, priority):
        self.description = description
        self.priority = priority.upper # Always uppercase

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        self.tasks.append(Task(description, priority)) #appending of type task
        return "Task added successfully."
    
    def __lt__(self, other):
        return Task.PRIORITY_MAP[self.priority] > Task.PRIORITY_MAP[other.priority]
        # returns tasks in order based on priority number
    
    #####
    ### keep an eye on this one. Have to check the pop tasks for correct index.
    ##### 

    def remove_task(self, index):
        value = ""
        if index < 1 or index > len(self.tasks):
            value = "Invalid task number"
        else:
            self.tasks.pop(index - 1) # Removes task
            value = "Removed task: {removed}"
        return value

    def show_all(self):
        if not self.tasks: # if there are no tasks
            result = "No tasks to show."
        else: 
            result = "Tasks:\n"
            for i, task in enumerate(self.tasks, start=1): # i is the num starting at 1, task is the task name
                result += f"{i}. {task}\n"
        return result
    
    def show_by_priority(self):
        sorted_tasks = sorted(self.tasks)  # Sorting uses __lt__ in Task class
        if not sorted_tasks:
            return "No tasks to show."
        result = "Tasks sorted by priority:\n"
        for i, task in enumerate(sorted_tasks, start=1):
            result += f"{i}. {task}\n"
        return result

def parse_command(command, todo_list):
    parts = command.split()
    if parts[0] == "ADD":
        task_start = command.index('"') + 1
        task_end = command.index('"', task_start)
        description = command[task_start:task_end]
        priority = "MEDIUM"
        if "PRIORITY" in parts:
                priority_index = parts.index("PRIORITY") + 1
                priority = parts[priority_index]
            return todo_list.add_task(description, priority)
        except ValueError:
            return "Invalid ADD command format."
        elif parts[0] == "REMOVE":
        try:
            index = int(parts[2])
            return todo_list.remove_task(index)
        except (IndexError, ValueError):
            return "Invalid REMOVE command format."
    elif parts[0] == "SHOW":
        if parts[1] == "ALL":
            return todo_list.show_all()
        elif parts[1] == "BY" and parts[2] == "PRIORITY":
            return todo_list.show_by_priority()
        else:
            return "Invalid SHOW command."
    else:
        return "Unknown command."
