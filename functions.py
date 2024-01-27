FILEPATH = "todos.txt"


# Define the function to read todos from the file
def get_todolist(fpath=FILEPATH):   # default argument
    with open(fpath, 'r') as file_opn:   # context manager function
        read_list = file_opn.readlines()    # read stored data into a list
    return read_list


# Define the function to write to the file
def write_todolist(fpath, todolist_arg):
    with open(fpath, "w") as file_opn:   # context manager function
        file_opn.writelines(todolist_arg)   # write user inputs into file


