import logging
from user_auth.password_utils import check_strength, generate_password, password_guidelines
from data.users import users, failed_attempts

def user_registration():
    username = input("Create a username: ")

    if username in users:
        logging.warning(f"Attempted registration with existing username: {username}")
        print("⚠️ This Username already exists!")
        return

    print("Create a password:")
    password_guidelines()

    while True:
        print("1. Enter your own password")
        print("2. Generate a strong random password")
        print("------------------------------")
        choice = input("Enter choice: ")
        print("------------------------------")

        if choice == "1":
            password = input("Create a password: ")
            strength = check_strength(password)
            print(f"Here is your Generated password: {strength}")
            if strength == "Strong":
                break
            else:
                print("⚠️ Password not strong enough. Please try again.\n")
                continue

        elif choice == "2":
            while True:
                password = generate_password()
                print(f"Here is your Generated password: {password}")

                strength = check_strength(password)
                print(f"Strength of your generated password is: {strength}")

                if strength == "Strong":
                    print("------------------------------------------------------------")
                    satisfied = input("Do you want to keep this password? (y/n): ")
                    print("------------------------------------------------------------")

                    if satisfied.lower() == "y":
                        break

                    else:
                        print("\nReturning to password options...\n")
                        break

                else:
                    print("⚠️ Generated password not strong enough, generating again...")
                    continue

            if strength == "Strong" and satisfied.lower() == "y":
                break

            else:
                continue

        else:
            print("You made an invalid choice!, try again.")

    users[username] = password
    failed_attempts[username] = 0
    logging.info(f"New user registered succeessfully: {username}")
    print(f"✅  {username} User registered successfully!\n")

