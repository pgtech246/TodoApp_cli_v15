FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Create a list object from items in a .txt"""
    with open(filepath, "r") as file_local:
            todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """Write list items to a .txt"""
    with open(filepath, "w") as file_local:
            file_local.writelines(todos_local)
