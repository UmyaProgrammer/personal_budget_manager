import json


class CreateUser:
    """
    A class that is meant to return and store user information.
    """
    def __init__(self):
        self.file = "users.json"
        self.users = self.get_users()


    def file_empty(self) -> bool:
        """
        Check whether the file is empty or not.
        :return: returns True if the file empty, False otherwise.
        """
        try:
            with open(self.file, "r") as file:
                json.load(file)

        except json.decoder.JSONDecodeError:
            return True

        else:
            return False


    def get_users(self) -> dict:
        """
        No parameters required.
        :return: A dictionary with all the users.
        """
        if not self.file_empty():
            with open(file=self.file, mode="r") as file:
                data = json.load(file)

            return data
        else:
            return {"error": "File empty!"}


    def add_user(self, name: str, password: str) -> None:
        """
        Creates a User from user inputs.
        :param name: username for the account.
        :param password: user password for the account.
        :return: None
        """

        dictionary_of_users = self.get_users()

        new_user = {
            f"user{len(dictionary_of_users)}": {
                "name": name,
                "password": password
            }
        }


        dictionary_of_users.update(new_user)

        json_object = json.dumps(dictionary_of_users, indent=4)


        with open(file=self.file, mode="r+") as file:
            file.write(json_object)


        self.users = self.get_users()



    def get_usernames(self) -> list:
        """
        Uses the file instance of the User class to get information from the users file.
        :return: A dictionary consisting of usernames
        """

        if not self.file_empty():
            list_of_usernames = []
            with open(self.file, "r") as file:
                data = json.load(file)
                for item in data.values():
                    list_of_usernames.append(item['name'])

        else:
            return []
        return list_of_usernames


    def find_user(self, name: str) -> bool:
        """
        Creates a list using self.print_usernames and uses the list to find if the user exists.
        :param name: username to check.
        :return: True if users exists, False otherwise.
        """

        list_of_usernames = self.get_usernames()

        if name in list_of_usernames:
            return True

        return False


    def varify(self, username: str, password: str) -> bool:
        """
        Verifies whether the username and password are correct.
        :param username: Username of the account.
        :param password: Password of the account.
        :return: True if the username and password match, false otherwise.
        """
        verified = False

        for user in self.users.values():

            if user['name'] == username:
                if user['password'] == password:
                    verified = True

        return verified














