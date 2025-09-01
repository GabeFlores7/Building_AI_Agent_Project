from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

# script for running tests to ensure get_files_info works correctly
if __name__ == "__main__":

    # Used to test get_files_info(working_directory, file_path)
    """
    print("Result for current directory:")
    print(get_files_info("calculator", "."))

    print("Result for 'pkg':")
    print(get_files_info("calculator", "pkg"))

    print("Result for '/bin':")
    print(get_files_info("calculator", "/bin"))

    print("Result for '../':")
    print(get_files_info("calculator", "../"))
    """
    # Used to test get_file_content(working_directory, filepath)

    # Test if get_file_content truncates correctly to MAX_CHAR limit
    # print(get_file_content("calculator", "lorem.txt"))

    
    print("Result for 'main.py' within 'calculator' directory:")
    print(get_file_content("calculator", "main.py"))

    print("\nResult for 'pkg/calculator.py':")
    print(get_file_content("calculator", "pkg/calculator.py"))

    print("\nResult for '/bin/cat':")
    print(get_file_content("calculator", "/bin/cat"))

    print("\nResult for 'pkg/does_not_exist.py':")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

