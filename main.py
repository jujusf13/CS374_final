from todo import ToDoList, parse_command

#Pat Tormey --> main file
def main():
    todo_list = ToDoList()
    print("Your to do list manager!!")
    print("Enter commands like: ADD TASK \"Finish project\" PRIORITY HIGH")
    print("Type EXIT to quit.")
    while True:
        command = input("> ")
        if command.strip().upper() == "exit":
            print("Goodbye!")
            break
        output = parse_command(command, todo_list)
        print(output)

if __name__ == "__main__":
    main()
