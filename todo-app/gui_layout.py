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
        [sg.InputText(todo_text, key="edit_todo", size=(40, 1))],
        [sg.Button(SAVE_EVENT), sg.Button("Cancel")]
    ]
    return sg.Window("Edit Todo", layout, modal=True, resizable=True, size=(400, 150))

def create_todo_row(todo, index):    return [
        sg.Text(f"{index + 1}.", size=(3, 1)),
        sg.Text(todo, size=(30, 1), key=f"{TODOS_KEY}{index}"),
        sg.Button("✓", key=f"{COMPLETE_EVENT}{index}", button_color=('white', 'green')),
        sg.Button("✎", key=f"{EDIT_EVENT}{index}", button_color=('black', 'white'))
    ]

def create_window():
    # Header section
    header_layout = [
        [sg.Text("Type in a to-do")],
        [sg.InputText(tooltip="Enter todo", key="todo", expand_x=True), sg.Button(ADD_EVENT)]
    ]
    
    # Get initial todos
    todos = functions.get_todos()
    
    # Create scrollable todos section with proper expansion
    todos_layout = [create_todo_row(todo, i) for i, todo in enumerate(todos)]    
    todos_frame = sg.Frame('', 
                          [[sg.Column(todos_layout,
                                    scrollable=True,
                                    expand_x=True,
                                    expand_y=True,
                                    key=TODOS_KEY)]],
                          expand_x=True,
                          expand_y=True,
                          border_width=0)

    # Combine all sections
    layout = header_layout + [[todos_frame]]

    window = sg.Window('My To-Do App',
                      layout,
                      resizable=True,
                      size=(500, 400),
                      margins=(10, 10))
    return window
