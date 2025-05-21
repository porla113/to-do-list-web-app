# get_todos function
def get_todos(filepath):
    """
    Read a text file and return a list of to-do items
    Arguments:
    - filepath - string
    Return:
    - a list of string
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

# write_todos function
def write_todos(filepath, todos_list):
    """
    Write a list of to-do items to a text file
    Arguments:
    - filepath: string
    - todos_list: a list of string
    Return:
    - None
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_list)