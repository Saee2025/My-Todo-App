import streamlit as st
import functions
todos=functions.todo_list()
def add_todo():
    todo=st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my first app")
st.write("This will increase your productivity !!")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="add a todo",
              on_change=add_todo ,key='new_todo')
st.session_state