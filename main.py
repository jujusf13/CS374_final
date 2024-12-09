from todo import ToDoList, parse_command

def main():
    todo_list = ToDoList()
    print("Welcome to the To-Do List Command Language!")
    print("Enter commands like: ADD TASK \"Finish project\" PRIORITY HIGH")
    print("Type EXIT to quit.")
    while True:
        command = input("> ")
        if command.strip().upper() == "EXIT":
            print("Goodbye!")
            break
        response = parse_command(command, todo_list)
        print(response)

if __name__ == "__main__":
    main()
