from functions.get_files_info import get_files_info # import custom fxn

# script for running tests to ensure get_files_info works correctly
if __name__ == "__main__":

    print("Result for current directory:")
    print(get_files_info("calculator", "."))

    print("Result for 'pkg':")
    print(get_files_info("calculator", "pkg"))

    print("Result for '/bin':")
    print(get_files_info("calculator", "/bin"))

    print("Result for '../':")
    print(get_files_info("calculator", "../"))