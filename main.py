import functions
import streamlit as st

filepath = "todos.txt"
todos = functions.get_todos(filepath)

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(filepath, todos)

st.title("To-do App")
st.subheader("This is a to-do web application.")
st.write("This app is to increase your productivity.")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo:", placeholder="Add new to-do...",
              on_change=add_todo, key='new_todo')

st.session_state