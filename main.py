from login import *
from file_managment import *

# Naor Ezra 205923758 && Shira Alon 316165026 class : 45.2


ADD_FILE_INTO_ANOTHER_FILE = '1'  # Section 1
DELETE_FILE = '2'  # Section 2
SWAP_CONTENT_SECOND_TO_FIRST = '3'  # Section 3
DELETE_WORD_FROM_FILE = '4'  # Section 4
EXIT = '5'  # Section 5


def print_menu() -> None:
    """
     function print the menu
     :return: None
    """
    print("\nEnter your choice : \n1 To Add content from the first file to second file \n"
          "2 To Deleting a file \n"
          "3 To Replace second file content with first file content \n"
          "4 To Delete all instances of a word in a file \n"
          "5 To exit from the program \n-> ", end="")


def sign_in() -> None:
    """
    function get username & password from the user, and try to log in.
    :return: None
    """
    while True:
        # Request a username and password from the user
        user_name = input("Enter user name : ")
        user_password = input("Enter user password : ")
        if login(user_name, user_password):  # Check that the username and password are correct
            print("Welcome, " + user_name + "!")
            break
        else:
            print('Invalid username or password, try again.')


def general() -> None:
    """
    function call to print menu func and ask to user to choose option and start func with that option
    :return:None
    """

    connected = True
    while connected:

        print_menu()
        user_choice = input()

        if user_choice == ADD_FILE_INTO_ANOTHER_FILE:
            add_one_file_to_another_file()

        elif user_choice == DELETE_FILE:
            delete_file()

        elif user_choice == SWAP_CONTENT_SECOND_TO_FIRST:
            swap_content_second_to_first()

        elif user_choice == DELETE_WORD_FROM_FILE:
            delete_word()

        elif user_choice == EXIT:
            # Update flag to finish the program
            connected = False

        else:
            print("Wrong choice try again.")

    print("Thank you for using our file management program. Exiting")


def main() -> None:
    """
    function main to start program
    :return: None
    """
    sign_in()
    general()


if __name__ == "__main__":
    main()
