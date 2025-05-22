import functions
import streamlit as st

filepath = "todos.txt"
csv_filepath = "todos.csv"

todos = functions.get_todos(filepath)
todos_csv = functions.get_todos_csv(csv_filepath)

def add_button_clicked():

    new_todo = st.session_state["new_todo"]
    complete_date = st.session_state["complete_date"].strftime("%d %b %Y")
    complete_time = st.session_state["complete_time"].strftime("%H:%M")

    todo_list = [todo['to-do'] for todo in todos_csv]

    # Check user to-do input
    if len(new_todo) == 0:
        print("Type a to-do")
    else:
        todo_dict = {}
        todo_dict['to-do'] = new_todo
        todo_dict['date'] = complete_date
        todo_dict['time'] = complete_time

        if todo_dict in todos_csv:
            print("already in todos")
            # st.session_state["new_todo"] = ""
        else:
            todos_csv.append(todo_dict)
            functions.write_todos_csv(csv_filepath, todos_csv)

            st.session_state["new_todo"] = ""

            # print(todo_dict)

def done_button_clicked():

    # Get a list of checked to-do
    checked_todo_index = []
    for key in st.session_state:
        if "-chbx" in key and st.session_state[key] is True:
            checked_todo_index.append(key.replace('-chbx',''))

    checked_todo_index = [int(index) for index in checked_todo_index]
    
    # Remove checked to-do from todos_csv list
    for index in checked_todo_index:
        todos_csv.pop(index)

        # Write to csv file
        functions.write_todos_csv(csv_filepath, todos_csv)

st.title("To-do App")
st.subheader("This is a to-do web application.")
st.write("This app is to increase your productivity.")

# To-do list section
col_A1, col_A2, col_A3 = st.columns(3)

with col_A1:
    st.subheader("To-do")
    for index, todo in enumerate(todos_csv):
        # checkbox = st.checkbox(todo['to-do'], key=f"{todo['to-do']}-chbx")
        checkbox = st.checkbox(todo['to-do'], key=f"{index}-chbx")

with col_A2:
    st.subheader("Date")
    for index, todo in enumerate(todos_csv):
        date_text = st.write(todo['date'])

with col_A3:
    st.subheader("Time")
    for index, todo in enumerate(todos_csv):
        time_text = st.write(todo['time'])

# Add section
col_B1, col_B2, col_B3 = st.columns(3)

with col_B1:
    st.text_input(label="Enter a todo:", placeholder="Add new to-do...",
                key='new_todo')

with col_B2:
    st.date_input(label="Date", value="today", format="DD/MM/YYYY", key="complete_date")

with col_B3:
    st.time_input(label="Time", value="now", step=300, key="complete_time")

# Buttons
st.button(label="Add", on_click=add_button_clicked, key="add_button")
st.button(label="Done", on_click=done_button_clicked, key="done_button")

# For debugging

# st.session_state