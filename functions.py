path = "todos.txt"


def get_todos(filepath=path):
    """Read the text file and return the list of to-do items"""
    with open(path, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=path):
    """Write to-do items list in the text file."""
    with open(path, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    pass