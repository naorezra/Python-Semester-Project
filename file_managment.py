import os


# Naor Ezra 205923758 && Shira Alon 316165026 class : 45.2


def valid_to_read_or_write(path: str, mode: str) -> bool:
    """
    function check if a file exists & it's valid to read & write into it.

    :param path: a path to the file
    :param mode: a mode to open the file
    :return: True if the file exists and has a valid permission else return False
    """
    # Try opening the file with the permission we received
    try:
        with open(path, mode):
            return True

    except PermissionError:
        print(f'No permission to {path}')
    except FileNotFoundError:
        print(f'file {path} does not exist.')

    return False


def check_if_file_not_empty(file_path: str) -> bool:
    """
    :param file_path: Get a file path
    :return: Return False if the file is empty and True if not
    """
    if not valid_to_read_or_write(file_path, 'r'):
        return False

    # open file in read mode
    with open(file_path, 'r') as f:
        f.read()
        # if the file handle is in place 0, the file is empty
        if f.tell() == 0:
            print(f'{file_path} is empty')
            return False
        return True


def add_one_file_to_another_file() -> None:     # Section 1
    """
    The function adds the contents of a first file to a second file.
    :return: None
    """
    # get path file from user
    src = input('Enter src file: ')
    dst = input('Enter dst file: ')
    # Check if the files are valid and the first file is not empty
    if valid_to_read_or_write(src, 'r') and valid_to_read_or_write(dst, 'a+') and check_if_file_not_empty(src):
        with open(src, 'r') as f:
            data = f.read()  # Copy the contents of a file
        with open(dst, 'a+') as f:
            f.write(data)  # appending the contents of the first file to the second file
            f.seek(0)  # relocating the pointer to the beginning of the file
            print("content of file after appending :\n" + f.read())


def delete_file() -> None:   # Section 2
    """
    The function asks the user for a file path and deletes it if possible
    :return:None
    """

    file_to_delete = input("Enter a path of the file to remove : ")

    try:
        if os.path.exists(file_to_delete):  # check if exists
            if os.path.isfile(file_to_delete):  # check if is a file
                os.remove(file_to_delete)  # Delete file
                print('File removed successfully!')
            else:
                print(f'Error. {file_to_delete} Is not a file type!')
        else:
            print(f'{file_to_delete} does not exists!')
    except PermissionError:
        print('No permission to delete the file...')
    except OSError:
        print("Error. System operation error")


def swap_content_second_to_first() -> None:  # Section 3
    """
    The function replaces the contents of the second file with the contents of the first file.
    :return:None
    """

    # get path file from user
    src = input('Enter first file: ')
    dst = input('Enter second file: ')
    # Check if the files are valid
    if valid_to_read_or_write(src, 'r') and valid_to_read_or_write(dst, 'w'):
        with open(src, 'r') as f_1:
            data_one = f_1.read()  # Copy the contents of a file
        with open(dst, 'w') as f_2:
            f_2.write(data_one)  # overrate the input file with the resulting data


def delete_word() -> None:     # Section 4
    """
     The function asks the user for a path of a file and a word (lower case) and deletes all instances of
     the word from the file
    :return:None
    """

    file_to_delete_words_from_it = input("Enter the file path from which you want to delete all instances of the word:")
    word_to_delete = input("Enter a word you wanna delete from the file (only lowercase letters) : ")

    if not (word_to_delete == word_to_delete.lower()):  # Check if the word is in lower case
        print('The word is not only lowercase.')
        return
    # Check if file valid
    if valid_to_read_or_write(file_to_delete_words_from_it, 'r+'):
        with open(file_to_delete_words_from_it, 'r') as f:  # open file in read mode
            # Copy the contents of a file and replace all occurrences of the word
            data = f.read().replace(word_to_delete, '')
        with open(file_to_delete_words_from_it, 'w') as f:  # open file in write mode
            f.write(data)  # overrate the input file with the resulting data
