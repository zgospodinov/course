import os

# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILEPATH = os.path.join(SCRIPT_DIR, 'todos.txt')

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
