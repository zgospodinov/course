def show_todos():
    print("\nYour todos:")
    for index, todo in enumerate(todos, 1):
        print(f"{index}. {todo}")

todos = []

while True:
    user_action = input("Type add, show, edit, or exit: ").strip().lower()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            show_todos()
        case "edit":
            show_todos()
            try:
                number = int(input("Enter the number of the todo you want to edit: "))
                if 1 <= number <= len(todos):
                    new_todo = input("Enter the new todo: ")
                    todos[number - 1] = new_todo
                    print("Todo updated successfully!")
                else:
                    print("Invalid todo number!")
            except ValueError:
                print("Please enter a valid number.")
        case "exit":
            print("Exiting the todo app. Goodbye!")
            break
        case _:
            print("Unknown command. Please type add, show, edit, or exit.")
