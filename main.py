import functions
import streamlit as st

filepath = "todos.txt"
todos = functions.get_todos(filepath)

def check_todo_input():
    todo = st.session_state["new_todo"] + "\n"
    
    if todo in todos:
        print("already in todos")
        st.session_state["new_todo"] = ""
    else:
        print("not in todos")
        add_todo()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(filepath, todos)
    st.session_state["new_todo"] = ""

st.title("To-do App")
st.subheader("This is a to-do web application.")
st.write("This app is to increase your productivity.")

# To-do checkbox list
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(filepath, todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo:", placeholder="Add new to-do...",
              on_change=check_todo_input, key='new_todo')

# For debugging
# st.session_state