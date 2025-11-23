import logging
import data.users as data_of_users
from user_auth.register import user_registration
from user_auth.login import login
from file_integrity.file_add import file_add
from file_integrity.file_verification import file_verification

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='security_toolkit.log',
    filemode='a'
)

def menu():
    while True:
        print("---------------------------------")
        print("    Login/Register Menu    ")
        print("---------------------------------")
        print("⚠️ Note : If you fail login 3 times, your account will get locked for 30 seconds.")
        print("1. Login with existing credentials?")
        print("2. New User? Just click here to register and continue.")
        print("3. Exit the Program")
        print("---------------------------------")
        choice = input("Enter your choice: ")
        print("---------------------------------")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if login(username, password):
                while data_of_users.user_logged_in:
                    print("---------------------------------")
                    print("    Security Toolkit    ")
                    print("---------------------------------")
                    print("1. Add this file to file integrity checker.")
                    print("2. Verify file integrity of the selected fie.")
                    print("3. Logout")
                    print("---------------------------------")
                    sub_choice = input("Enter choice: ")
                    print("---------------------------------")

                    if sub_choice == "1":
                        filename = input("Enter filename: ")
                        file_add(filename)

                    elif sub_choice == "2":
                        filename = input("Enter filename: ")
                        file_verification(filename)

                    elif sub_choice == "3":
                        logging.info(f"{data_of_users.user_logged_in} logged out of the security toolkit.")
                        print("Logging out...")
                        data_of_users.user_logged_in = None
                        break

                    else:
                        print("That's not a valid choice!")
        elif choice == "2":
            user_registration()

        elif choice == "3":
            print("Goodbye! Have a nice day.")

            break

        else:
            print("Oops! That's not a valid choice. Try again?")

menu()

