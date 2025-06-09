from functions import get_todos, save_todos, show_todos

todos = get_todos()

while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip().lower()

    match user_action:
        case "add":
            todos.append(input("Enter a todo: "))
            save_todos(todos)
        case "show":
            show_todos(todos)
        case "edit":
            show_todos(todos)
            try:
                number = int(input("Enter the number of the todo you want to edit: "))
                if 1 <= number <= len(todos):
                    todos[number - 1] = input("Enter the new todo: ")
                    save_todos(todos)
                    print("Todo updated successfully!")
                else:
                    print("Invalid todo number!")
            except ValueError:
                print("Please enter a valid number.")
        case "complete":
            show_todos(todos)
            try:
                number = int(input("Enter the number of the todo to complete: "))
                if 1 <= number <= len(todos):
                    removed_todo = todos.pop(number - 1)
                    save_todos(todos)
                    print(f"Todo '{removed_todo}' was completed and removed from the list!")
                else:
                    print("Invalid todo number!")
            except ValueError:
                print("Please enter a valid number.")
        case "exit":
            print("Exiting the todo app. Goodbye!")
            break
        case _:
            print("Unknown command. Please type add, show, edit, complete, or exit.")
