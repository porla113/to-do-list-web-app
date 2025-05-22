import csv

# get_todos_csv function
def get_todos_csv(csv_filepath):
    """
    Read a csv file and return a list of to-do dict (to-do, date, time)
    Arguments:
    - csv_filepath - string
    Return:
    - a list of to-do dict
    """
    todos = []
    with open(csv_filepath) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            todos.append(row)
    return todos

# write_todos_csv function
def write_todos_csv(csv_filepath, todos_list):
    """
    Write a list of to-do dict (to-do, date, time) to a csv file
    Arguments:
    - csv_filepath: string
    - todos_list: a list of to-do dict
    Return:
    - None
    """
    with open(csv_filepath, 'w', newline='') as csv_file:
        fieldnames = ['to-do', 'date', 'time']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        csv_writer.writeheader()
        for row in todos_list:
            csv_writer.writerow(row)

    return  None

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