import streamlit as st
import functions

st.title("My To Do App")
st.subheader("This app is to increase your productivity")

if "new_todo" not in st.session_state:
    st.session_state["new_todo"] = ""

todos = functions.get_todos()
def add_todo():

    new_todo = st.session_state["new_todo"].strip()  # Remove any leading/trailing spaces
    if new_todo:  # Only add non-empty todos
        todos.append(new_todo + "\n")
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""
        st.rerun()

def update_todos(index):
    todos.pop(index)
    functions.write_todos(todos)
    st.rerun()  # Refresh the app to reflect the changes


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")
    if checkbox:
        update_todos(index)
        del st.session_state[todo]
st.text_input(label=" ", placeholder="Add new todo.....",
              on_change=add_todo(), key="new_todo")

