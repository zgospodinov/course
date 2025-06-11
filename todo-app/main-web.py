import streamlit as st
import functions


def add_todo():
    todo = st.session_state.todo_input
    if todo:
        try:
            st.session_state.todos.append(todo)
            functions.save_todos(st.session_state.todos)
            st.session_state.todo_input = ""
            # st.rerun()
        except Exception as e:
            st.error(f"Error saving todo: {str(e)}")
    else:
        st.warning("Please enter a todo before adding.")

st.title("Todo App")
st.write("Todo app to increase your productivity")
st.text_input("", placeholder="Add a new todo", key="todo_input", on_change=add_todo)

if 'todos' not in st.session_state:
    try:
        st.session_state.todos = functions.get_todos()
    except Exception as e:
        st.error(f"Error loading todos: {str(e)}")
        st.session_state.todos = []

for index, todo in enumerate(st.session_state.todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")
    if checkbox:
        st.session_state.todos.pop(index)
        functions.save_todos(st.session_state.todos)
        st.rerun()


