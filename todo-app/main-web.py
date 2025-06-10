import streamlit as st
import functions

st.title("Todo App")
st.write("Todo app to increase your productivity")
st.text_input("", placeholder="Add a new todo", key="todo_input")

try:
    todos = functions.get_todos()
except Exception as e:
    st.error(f"Error loading todos: {str(e)}")
    todos = []

for todo in todos:
    st.checkbox(todo, key=todo)



