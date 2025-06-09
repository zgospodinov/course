import FreeSimpleGUI as sg
import functions

ADD_EVENT = "Add"
EDIT_EVENT = "Edit"
SAVE_EVENT = "Save"
TODOS_KEY = "-TODOS-"

def create_edit_popup(todo_text):
    layout = [
        [sg.Text("Edit todo:")],
        [sg.InputText(todo_text, key="edit_todo")],
        [sg.Button(SAVE_EVENT), sg.Button("Cancel")]
    ]
    return sg.Window("Edit Todo", layout, modal=True)

def create_window():
    label = sg.Text("Type in a to-do")
    input_box = sg.InputText(tooltip="Enter todo", key="todo")
    add_button = sg.Button(ADD_EVENT)
    edit_button = sg.Button(EDIT_EVENT)
    todos_list = sg.Listbox(values=functions.get_todos(), 
                           key=TODOS_KEY,
                           size=(40, 10))

    window = sg.Window('My To-Do App',
                      layout=[[label],
                             [input_box, add_button, edit_button],
                             [todos_list]])
    return window
