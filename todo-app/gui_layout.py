import FreeSimpleGUI as sg
import functions

ADD_EVENT = "Add"
TODOS_KEY = "-TODOS-"

def create_window():
    label = sg.Text("Type in a to-do")
    input_box = sg.InputText(tooltip="Enter todo", key="todo")
    add_button = sg.Button(ADD_EVENT)
    todos_list = sg.Listbox(values=functions.get_todos(), 
                           key=TODOS_KEY,
                           size=(40, 10))

    window = sg.Window('My To-Do App',
                      layout=[[label],
                             [input_box, add_button],
                             [todos_list]])
    return window
