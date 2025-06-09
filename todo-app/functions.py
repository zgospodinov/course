FILEPATH = 'todo-app/todos.txt'

def get_todos(filepath=FILEPATH):
    try:
        with open(filepath, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_todos(todos_list, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        for todo in todos_list:
            file.write(todo + '\n')

def show_todos(todos):
    print("\nYour todos:")
    for index, todo in enumerate(todos, 1):
        print(f"{index}. {todo}")
