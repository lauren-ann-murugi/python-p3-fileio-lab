# lib/file_io.py

def write_file(file_name, file_content):
    """
    Writes the provided content to a .txt file.
    Overwrites if the file already exists.
    """
    # Ensure the filename ends with .txt
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, "w") as file:
        file.write(file_content)


def append_file(file_name, append_content):
    """
    Appends the provided content to an existing .txt file.
    Creates the file if it does not exist.
    """
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, "a") as file:
        file.write(append_content)


def read_file(file_name):
    """
    Reads and returns the content of a .txt file.
    """
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, "r") as file:
        return file.read()