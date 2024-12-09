class Task:
    def __init__ (self, description, priority):
        self.description = description
        self.priority = priority.upper # Always uppercase

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        self.tasks.append(Task(description, priority)) #appending of type task
        return "Task added successfully."
    
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