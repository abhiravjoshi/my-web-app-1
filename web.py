import streamlit as st
import functions
import os

todos = functions.get_todos("todos.txt")
if not os.path.exists("todos.txt"):
    with open("todos.txt",'w') as file:
        pass


def add_todo():
    todo_local = st.session_state["new_todo"]
    todos.append(todo_local + '\n')
    functions.set_todos(todos)
    st.session_state["new_todo"] = ''


st.title("My Todo App")
st.subheader("This is my To-Do list app.")
for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip(),key=f"todo-{i+1}")
    if checkbox:
        # print(checkbox)
        todos.pop(i)
        functions.set_todos(todos)
        del st.session_state[f"todo-{i+1}"]
        st.experimental_rerun()


st.text_input("Enter a new todo:",
              placeholder='Type here...',
              on_change=add_todo, key='new_todo')
# print(form)

# st.session_state
# print(i)