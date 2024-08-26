"""
hero.py

This module contains classes representing different types of human characters
in a game, such as Human, Archer, Knight, and Wizard. Each class has attributes
for health, stamina, speed, level, and attack capabilities, as well as methods
to simulate attacking and health checking.
"""

from datetime import datetime, timedelta


class Human:
    """
    A base class to represent a human character in the game.

    Attributes:
    ----------
    title : str
        The title or role of the character
    hp : int
        The health points of the character
    stamina : int
        The stamina level of the character
    speed : int
        The speed of the character
    level : int
        The level of the character
    attack : int
        The attack power of the character
    reload_time : int
        The reload time between attacks in microseconds
    last_attack : datetime or None
        The timestamp of the last attack made by the character
    """

    def __init__(self, title, hp, stamina, speed, level, attack, reload_time):
        """
        Initializes the Human class with attributes for title, health, stamina,
        speed, level, attack power, and reload time.

        Parameters:
        ----------
        title : str
            The title or role of the character
        hp : int
            The health points of the character
        stamina : int
            The stamina level of the character
        speed : int
            The speed of the character
        level : int
            The level of the character
        attack : int
            The attack power of the character
        reload_time : int
            The reload time between attacks in microseconds
        """
        self.title = title
        self.hp = hp
        self.stamina = stamina
        self.speed = speed
        self.level = level
        self.attack = attack
        self.reload_time = reload_time
        self.last_attack = None

    def __str__(self):
        """
        Returns a string representation of the Human object.

        Returns:
        -------
        str
            A string describing the character's race.
        """
        return f"Race: {self.title}"

    def check_attack(self):
        """
        Checks if the character can attack again based on the reload time.

        Returns:
        -------
        bool
            True if the character can attack, False otherwise.
        """
        if self.last_attack and datetime.now() - self.last_attack < timedelta(
            microseconds=self.reload_time
        ):
            return False
        else:
            return True

    def attack_func(self):
        """
        Simulates the attack action of the character.

        Returns:
        -------
        int
            The attack power if the character can attack, otherwise 0.
        """
        if self.check_attack():
            self.last_attack = datetime.now()
            print(f"Attacking with power {self.attack}")
            return self.attack
        else:
            print("Please, wait")
            return 0

    def hell_check(self):
        """
        Checks the character's health and prints a message if the character is dead.
        """
        if self.hp <= 0:
            print("Enemy dead")


class Archer(Human):
    """
    A class to represent an Archer character, inheriting from Human.
    """

    def __init__(self, level):
        """
        Initializes the Archer with default stats based on the level.

        Parameters:
        ----------
        level : int
            The level of the Archer character.
        """
        self.title = "Archer"
        super().__init__(
            self.title, 80 + level * 20, 95 + level * 5, 3, level, 40 + level * 5, 300
        )


class Knight(Human):
    """
    A class to represent a Knight character, inheriting from Human.
    """

    def __init__(self, level):
        """
        Initializes the Knight with default stats based on the level.

        Parameters:
        ----------
        level : int
            The level of the Knight character.
        """
        self.title = "Knight"
        super().__init__(
            self.title, 80 + level * 20, 95 + level * 5, 3, level, 40 + level * 5, 200
        )


class Wizard(Human):
    """
    A class to represent a Wizard character, inheriting from Human.
    """

    def __init__(self, level):
        """
        Initializes the Wizard with default stats based on the level.

        Parameters:
        ----------
        level : int
            The level of the Wizard character.
        """
        self.title = "Wizard"
        super().__init__(
            self.title, 80 + level * 20, 95 + level * 5, 3, level, 40 + level * 5, 200
        )
