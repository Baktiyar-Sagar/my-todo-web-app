import streamlit as st
from streamlit import checkbox

import functions

def add_todo():
    todo = st.session_state["new_todo"]+ '\n'
    todo_list.append(todo)
    functions.write_todo(todo_list)

st.title("My To do App")
st.subheader("This is my todo app")
st.write("This app to increase my productivity" )

todo_list = functions.get_todos()

for index,todo in enumerate(todo_list):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todo_list.pop(index)
        functions.write_todo(todo_list)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="Add new todo....",key='new_todo',on_change=add_todo)

