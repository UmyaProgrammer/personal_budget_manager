from create_user import CreateUser
from user import User


logo = r"""
__________          .___              __       _____                                             
\______   \__ __  __| _/ ____   _____/  |_    /     \ _____    ____ _____     ____   ___________ 
 |    |  _/  |  \/ __ | / ___\_/ __ \   __\  /  \ /  \\__  \  /    \\__  \   / ___\_/ __ \_  __ \
 |    |   \  |  / /_/ |/ /_/  >  ___/|  |   /    Y    \/ __ \|   |  \/ __ \_/ /_/  >  ___/|  | \/
 |______  /____/\____ |\___  / \___  >__|   \____|__  (____  /___|  (____  /\___  / \___  >__|   
        \/           \/_____/      \/               \/     \/     \/     \//_____/      \/       
"""


def login() -> (bool, str):

    logged_in = False

    create_user_object = CreateUser()
    user_name = input("Please enter your username: ")

    if create_user_object.find_user(user_name):
        user_password = input("\tPlease enter your password: ")
        if create_user_object.varify(user_name, user_password):
            logged_in = True

        login_attempts = 5

        while not logged_in and login_attempts > 1:
            user_password = input("\tPlease enter your password: ")
            if create_user_object.varify(user_name, user_password):
                logged_in = True
            else:
                login_attempts -= 1

        if not logged_in:
            user_name = "failed to login hehe"


    else:
        print("\n")
        if input("Would you like to create a user?(y/n) ").lower() == "y":
            print(f"Your user name: {user_name}.")
            password = input("Enter a password: ")
            create_user_object.add_user(name=user_name, password=password)

        print(f"User successfully created: {create_user_object.find_user(user_name)}")
        logged_in = True

    print("\n")

    return logged_in, user_name


def main() -> bool:
    print(logo)
    print("Hello user!")

    successfully_login, username = login()

    if not successfully_login:
        print("Please restart, and make sure to get the your password right next time!")
        return False
    else:
        user = User(username)
        print(f"Welcome back user: '{user.user_name}'")
        log_out = False
        print("\nMenu Options:\n1. Add a transaction\n2. View all transactions\n3. View financial summary\n4. Exit")
        while not log_out:
            try:
                command = int(input("Option: "))

            except ValueError:
                print("\tPlease enter an integer!")
                print("\n")

            else:
                if command == 1:
                    print("\n")
                    print("1. Essentials\n2. Financial Responsibilities\n3. Discretionary\n4. Personal & Family\n5. Business & Work-Related")
                    print("\n")

                    user.make_transaction()
                elif command == 2:
                    user.see_all_transactions()
                elif command == 3:
                    user.get_summary()
                elif command == 4:
                    log_out = True
                else:
                    print("\tPlease enter integers (1-4).")
                    print("\n")

    user_continue = input("Would you like to continue?(y/n) ").lower()
    if user_continue == "y":
        return True
    else:
        return False



if __name__ == '__main__':
    playing = True
    while playing:
        playing = main()








