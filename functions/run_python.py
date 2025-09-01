import os
import sys
import subprocess

def run_python_file(working_directory, file_path, args=[]):

    # create abs paths for file path args
    abs_working_dir_path = os.path.abspath(working_directory)
    # if file_path is an absolute path convert to relative
    if os.path.isabs(file_path):
        file_path = os.path.relpath(file_path, abs_working_dir_path)
        
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # check if desired path is within working directory
    if os.path.commonpath([abs_working_dir_path, abs_file_path]) != abs_working_dir_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    # check if file file exists
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    # check if the file ends with '.py'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try: 
        # execute python file with subprocess run
        completed_process = subprocess.run(
            args = [sys.executable, abs_file_path, *args],
            capture_output= True,
            cwd = working_directory,
            timeout = 30,
            text = True
            )
        # capture completed process attributes
        out = completed_process.stdout
        err = completed_process.stderr
        return_code = completed_process.returncode
        # if stdout and stderr of execution were not captured
        if not out.strip() and not err.strip():
            return "No output produced."
        # build string to return attributes
        build_list = [f"STDOUT: {out}", f"STDERR: {err}"]
        # attach non-zero return code
        if return_code != 0:
            build_list.append(f"Process exited with code {return_code}")
            
        return "\n".join(build_list)

    except Exception as e:
        return f"Error: executing Python file: {e}"