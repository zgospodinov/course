import FreeSimpleGUI as sg

def create_window():
    label = sg.Text("Type in a to-do")
    input_box = sg.InputText(tooltip="Enter todo", key="todo")
    add_button = sg.Button("Add")

    window = sg.Window('My To-Do App',
                      layout=[[label], [input_box, add_button]])
    return window
