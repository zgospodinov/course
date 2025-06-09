import FreeSimpleGUI as sg
import functions

ADD_EVENT = "Add"
EDIT_EVENT = "Edit::"  # Prefix for edit button events
SAVE_EVENT = "Save"
COMPLETE_EVENT = "Complete::"  # Prefix for complete button events

TODOS_KEY = "-TODOS-"

def create_edit_popup(todo_text):
    layout = [
        [sg.Text("Edit todo:")],
        [sg.InputText(todo_text, key="edit_todo")],
        [sg.Button(SAVE_EVENT), sg.Button("Cancel")]
    ]
    return sg.Window("Edit Todo", layout, modal=True)

def create_todo_row(todo, index):    return [
        sg.Text(f"{index + 1}.", size=(3, 1)),
        sg.Text(todo, size=(30, 1), key=f"{TODOS_KEY}{index}"),
        sg.Button("✓", key=f"{COMPLETE_EVENT}{index}", button_color=('white', 'green')),
        sg.Button("✎", key=f"{EDIT_EVENT}{index}", button_color=('black', 'white'))
    ]

def create_window():
    label = sg.Text("Type in a to-do")
    input_box = sg.InputText(tooltip="Enter todo", key="todo")
    add_button = sg.Button(ADD_EVENT)
    
    # Get initial todos
    todos = functions.get_todos()
    # Create a column of todo rows
    todos_column = sg.Column(
        [[sg.Column([create_todo_row(todo, i) for i, todo in enumerate(todos)],
                   key=TODOS_KEY,
                   scrollable=True,
                   size=(400, 150))]]
    )

    window = sg.Window('My To-Do App',
                      layout=[[label],
                             [input_box, add_button],
                             [todos_column]])
    return window
