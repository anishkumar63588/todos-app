import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



st.title("Welcome to the To-do App")
st.subheader("This app will help you to increase your productivity.")


for todo in todos:
    st.checkbox(todo)

add_todo = st.text_input(label="", placeholder="Add a new to-do...",
                         on_change=add_todo, key='new_todo')

st.session_state
