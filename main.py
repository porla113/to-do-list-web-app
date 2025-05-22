import functions
import streamlit as st

filepath = "todos.txt"
csv_filepath = "todos.csv"

todos = functions.get_todos(filepath)
todos_csv = functions.get_todos_csv(csv_filepath)

def add_button_clicked():
    # print("add button clicked.")
    todo = st.session_state["new_todo"]
    todo_list = [todo['to-do'] for todo in todos_csv]
    if len(todo) == 0:
        print("Type a to-do")
    elif todo in todo_list:
        print("already in todos")
        # st.session_state["new_todo"] = ""
    else:
        new_todo = st.session_state["new_todo"]
        complete_date = st.session_state["complete_date"].strftime("%d %b %Y")
        complete_time = st.session_state["complete_time"].strftime("%H:%M")

        todo_dict = {}
        todo_dict['to-do'] = new_todo
        todo_dict['date'] = complete_date
        todo_dict['time'] = complete_time

        todos_csv.append(todo_dict)
        functions.write_todos_csv(csv_filepath, todos_csv)

        st.session_state["new_todo"] = ""

        print(todo_dict)
        # print(f"{str_todo_dict} added in todos")
        

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
        checkbox = st.checkbox(todo['to-do'], key=f"{todo['to-do']}-chbx")

        # if checkbox:
        #     todos_csv.pop(index)
        #     functions.write_todos_csv(csv_filepath, todos_csv)
        #     del st.session_state[todo['to-do']]
        #     st.rerun()
with col_A2:
    st.subheader("Date")
    for index, todo in enumerate(todos_csv):
        date_text = st.write(todo['date'])
with col_A3:
    st.subheader("Time")
    for index, todo in enumerate(todos_csv):
        time_text = st.write(todo['time'])
# To-do checkbox list
# for index, todo in enumerate(todos_csv):
#     label_text = f"{todo['to-do']}, {todo['date']}, {todo['time']}"
#     checkbox = st.checkbox(label_text, key=todo['to-do'])

col1, col2, col3 = st.columns(3)

with col1:
    # st.text_input(label="Enter a todo:", placeholder="Add new to-do...",
    #             on_change=check_todo_input, key='new_todo')
    st.text_input(label="Enter a todo:", placeholder="Add new to-do...",
                key='new_todo')
with col2:
    st.date_input(label="Date", value="today", format="DD/MM/YYYY", key="complete_date")
with col3:
    st.time_input(label="Time", value="now", step=300, key="complete_time")

st.button(label="Add", on_click=add_button_clicked, key="add_button")
# st.button(label="Edit", on_click=edit_button_clicked, key="edit_button")
st.button(label="Done", on_click=done_button_clicked, key="done_button")

# For debugging
st.session_state

checked_todo = []
for key in st.session_state:
    if "-chbx" in key and st.session_state[key] is True:
        # print(key)
        checked_todo.append(key)
    
# print(checked_todo)