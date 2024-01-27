import streamlit as st
import functions

# read todos.txt first (bef session)
todolist = functions.get_todolist("todos.txt")


# st.session.state is a sp object for session callbacks. Like dict
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    # append the new to-do to the list and write back
    todolist.append(todo)
    functions.write_todolist("todos.txt", todolist)


# Now, we render the items on the website in the order below
st.title("My Todo App")
st.subheader("This is my todo app")
st.write("this app is to increase your productivity")

# checkboxes
for index, todo_item in enumerate(todolist):
    # create checkboxes and assign a key to each box
    checkbox = st.checkbox(todo_item, key=todo_item)

    # if checkbox is checked, the checkbox["todo_item"] is true
    # this means to-do is completed, so we can delete it
    if checkbox:
        todolist.pop(index)              # delete the to-do which got done
        functions.write_todolist("todos.txt", todolist)
        del st.session_state[todo_item]  # delete to-do from session
        st.experimental_rerun()          # refresh the page


st.text_input(label="Enter a todo:",
              on_change=add_todo,
              key="new_todo")
