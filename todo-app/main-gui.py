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
        # Recreate todos column with updated list
        new_layout = [layout.create_todo_row(todo, i) for i, todo in enumerate(todos)]
        window[layout.TODOS_KEY].update(new_layout)
        window['todo'].update('')  # Clear the input field

    # Handle Edit button events
    if event.startswith(layout.EDIT_EVENT):
        # Extract the index from the event key
        index = int(event.split("::")[-1])
        todos = functions.get_todos()
        if 0 <= index < len(todos):
            todo_to_edit = todos[index]
            edit_window = layout.create_edit_popup(todo_to_edit)
            
            # Event loop for edit window
            while True:
                edit_event, edit_values = edit_window.read()
                if edit_event in (sg.WIN_CLOSED, "Cancel"):
                    edit_window.close()
                    break
                    
                if edit_event == layout.SAVE_EVENT:
                    todos = functions.get_todos()
                    todos[index] = edit_values["edit_todo"]
                    functions.save_todos(todos)
                    # Recreate todos column with updated list
                    new_layout = [layout.create_todo_row(todo, i) for i, todo in enumerate(todos)]
                    window[layout.TODOS_KEY].update(new_layout)
                    edit_window.close()
                    break

    # Handle Complete button events
    if event.startswith(layout.COMPLETE_EVENT):
        # Extract the index from the event key
        index = int(event.split("::")[-1])
        todos = functions.get_todos()
        if 0 <= index < len(todos):
            removed_todo = todos.pop(index)
            functions.save_todos(todos)
            # Recreate todos column with updated list
            new_layout = [layout.create_todo_row(todo, i) for i, todo in enumerate(todos)]
            window[layout.TODOS_KEY].update(new_layout)
 
window.close()