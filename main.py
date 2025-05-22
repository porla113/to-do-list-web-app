import functions
import streamlit as st

filepath = "todos.txt"
csv_filepath = "todos.csv"

todos = functions.get_todos(filepath)
todos_csv = functions.get_todos_csv(csv_filepath)

def add_button_clicked():
    print("add button clicked.")

def edit_button_clicked():
    print("edit button clicked.")
    # st.error("To-do is added!")

def done_button_clicked():
    print("done button clicked.")

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

col_A1, col_A2, col_A3 = st.columns(3)

with col_A1:
    st.subheader("To-do")
    for index, todo in enumerate(todos_csv):
        checkbox = st.checkbox(todo['to-do'], key=todo['to-do'])
        # if checkbox:
        #     todos_csv.pop(index)
        #     functions.write_todos_csv(csv_filepath, todos_csv)
        #     del st.session_state[todo['to-do']]
        #     st.rerun()
with col_A2:
    st.subheader("Date")
    for index, todo in enumerate(todos_csv):
        date_text = st.write(todo['date'], key=todo['date'])
with col_A3:
    st.subheader("Time")
    for index, todo in enumerate(todos_csv):
        time_text = st.write(todo['time'], key=todo['time'])
# To-do checkbox list
# for index, todo in enumerate(todos_csv):
#     label_text = f"{todo['to-do']}, {todo['date']}, {todo['time']}"
#     checkbox = st.checkbox(label_text, key=todo['to-do'])

col1, col2, col3 = st.columns(3)

with col1:
    st.text_input(label="Enter a todo:", placeholder="Add new to-do...",
                on_change=check_todo_input, key='new_todo')
with col2:
    st.date_input(label="Date", value="today", format="DD/MM/YYYY", key="complete_date")
with col3:
    st.time_input(label="Time", value="now", step=300, key="complete_time")

st.button(label="Add", on_click=add_button_clicked, key="add_button")
st.button(label="Edit", on_click=edit_button_clicked, key="edit_button")
st.button(label="Done", on_click=done_button_clicked, key="done_button")

# For debugging
st.session_state