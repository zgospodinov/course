import functions
import FreeSimpleGUI as sg
from gui_layout import create_window

window = create_window()

while True:
    event, values = window.read()
    print(event)
    print(values)

    if event == sg.WIN_CLOSED:
        break

    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo']
        todos.append(new_todo)
        functions.save_todos(todos)

window.close()