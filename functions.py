FILEPATH = "todos.txt"


def printList(todo_list):
    """ This will print the to-do list.
    """
    for index, item in enumerate(todo_list):
        item = item.strip('\n')
        print(f"{index + 1} - {item}")


def get_todos(fh=FILEPATH):
    """ This will return our to-do list after reading it
    from a backend txt file.
    """
    with open(fh, 'r') as file:
        todos_local = file.readlines()  # don't need to close the file anymore
    return todos_local


def set_todos(todos_local, fh=FILEPATH):
    """ This will write our to-do list back into the
    backend txt file.
    """
    with open(fh, 'w') as file:
        file.writelines(todos_local)  # don't need to close the file anymore

# print(__name__)
# in functions.py, it will show up as "__main__",
# when run in commandLineInterface.py, it will show up as "functions"
if __name__ == "__main__":
    print("Hello from functions")