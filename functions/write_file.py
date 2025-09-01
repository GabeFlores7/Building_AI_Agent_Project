import os

# function used to write and overwrite files
def write_file(working_directory, file_path, content):

    # create abs paths for file path args
    abs_desired_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir_path = os.path.abspath(working_directory)
    abs_file_parent_path = os.path.dirname(abs_desired_path)

    # check if desired file_path is not within working_directory
    if os.path.commonpath([abs_desired_path, abs_working_dir_path]) != abs_working_dir_path:
       return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
       
    # try checking and making path if non-existent
    try: 
        # create desired path and all parent directories
        if not os.path.exists(abs_file_parent_path):
            os.makedirs(abs_file_parent_path)
        # overwrite file contents with content arg
        with open(abs_desired_path, "w") as file:
            file.write(content)
    except Exception as e:
        return f"Error: {e}"
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'