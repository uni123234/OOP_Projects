class User:
    """
    A class to represent a user with personal details.

    Attributes:
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        age (int): The age of the user.
    """

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        """
        Initialize a new User instance.

        Args:
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            age (int): The age of the user.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_info(self) -> None:
        """
        Print the information of the user in a formatted string.
        """
        print(f"User {self.first_name} {self.last_name} (age = {self.age})")
