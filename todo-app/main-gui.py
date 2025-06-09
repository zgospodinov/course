import functions
import FreeSimpleGUI as sg
import gui_layout as layout

window = layout.create_window()

while True:
    event, values = window.read()
    print(event)
    print(values)

    if event == sg.WIN_CLOSED:
        break

    if event == layout.ADD_EVENT:
        todos = functions.get_todos()
        new_todo = values['todo']
        todos.append(new_todo)
        functions.save_todos(todos)
        window[layout.TODOS_KEY].update(values=todos)  # Refresh the listbox
 
window.close()