# filepath: c:\F\code\python-mega-course\course\todo-app\todos.txt
def get_todos():
    try:
        with open('todos.txt', 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_todos(todos_list):
    with open('todos.txt', 'w') as file:
        for todo in todos_list:
            file.write(todo + '\n')

def show_todos():
    print("\nYour todos:")
    for index, todo in enumerate(todos, 1):
        print(f"{index}. {todo}")

todos = get_todos()

while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip().lower()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
            save_todos(todos)
        case "show":
            show_todos()
        case "edit":
            show_todos()
            try:
                number = int(input("Enter the number of the todo you want to edit: "))
                if 1 <= number <= len(todos):
                    new_todo = input("Enter the new todo: ")
                    todos[number - 1] = new_todo
                    save_todos(todos)
                    print("Todo updated successfully!")
                else:
                    print("Invalid todo number!")
            except ValueError:
                print("Please enter a valid number.")
        case "complete":
            show_todos()
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
