import os
from config import MAX_CHARS

# Function responsible for retrieving file contents

def get_file_content(working_directory, file_path):
    # create abs paths for file path args
    abs_desired_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir_path = os.path.abspath(working_directory)
    # check if desired file_path is not within working_directory
    if not abs_desired_path.startswith(abs_working_dir_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    # check if file_path is not a file
    if not os.path.isfile(abs_desired_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    # read file and return contents as a string
    try:
        with open(abs_desired_path, "r") as file:
            content = file.read(MAX_CHARS + 1)
            if len(content) > MAX_CHARS:
                return content[0:MAX_CHARS] + f'[...File "{file_path}" truncated at 10000 characters]'
            else:
                return content
    except Exception as e:
        return f"Error: {e}"