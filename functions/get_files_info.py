import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

def get_files_info(working_directory, directory="."):
    # Create variables to store absolute paths of working dir and desired dir
    joined_path = os.path.join(working_directory, directory) 
    abs_joined_full_path = os.path.abspath(joined_path)
    working_dir_full_path = os.path.abspath(working_directory)

    # Ensure desired directory exists within working directory
    if not abs_joined_full_path.startswith(working_dir_full_path): # Check if dir is in working dir 
       return  f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(abs_joined_full_path):# check if directory exists
        return f'Error: "{directory}" is not a directory'
    
    try:
        # initialize variables to hold file descriptors
        contents_string = ""
        file_size = 0
        is_dir = False
        # for each item in directory
        for name in os.listdir(abs_joined_full_path):
            file_path = os.path.join(abs_joined_full_path, name)
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            # output string containing file name, size in bytes, and if it's a dir
            contents_string += f"- {name}: file_size={file_size} bytes, is_dir={is_dir}\n"
        return contents_string
    except Exception as e: # return error string if any errors occur
        return f"Error: {e}"


# Used to tell the LLM how to use the function

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)