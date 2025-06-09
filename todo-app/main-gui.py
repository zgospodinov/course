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
        window['todo'].update('')  # Clear the input field

    # Handle Edit button event
    if event == layout.EDIT_EVENT and len(values[layout.TODOS_KEY]) > 0:
        todo_to_edit = values[layout.TODOS_KEY][0]  # Get selected todo
        edit_window = layout.create_edit_popup(todo_to_edit)
        
        # Event loop for edit window
        while True:
            edit_event, edit_values = edit_window.read()
            if edit_event in (sg.WIN_CLOSED, "Cancel"):
                edit_window.close()
                break
                
            if edit_event == layout.SAVE_EVENT:
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = edit_values["edit_todo"]
                functions.save_todos(todos)
                window[layout.TODOS_KEY].update(values=todos)  # Refresh main window listbox
                edit_window.close()
                break
 
window.close()