"""
dog.py

This module contains the Dog class, which represents a dog with attributes
such as name, age, and weight. The class also includes a method for barking.
"""

class Dog:
    """
    A class to represent a dog.

    Attributes:
    ----------
    name : str
        The name of the dog
    age : int
        The age of the dog in years
    weight : float
        The weight of the dog in kilograms
    """

    def __init__(self, name: str, age: int, weight: float) -> None:
        """
        Initializes the Dog with a name, age, and weight.

        Parameters:
        ----------
        name : str
            The name of the dog
        age : int
            The age of the dog in years
        weight : float
            The weight of the dog in kilograms
        """
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self) -> None:
        """
        Prints a bark sound to the console.
        """
        print("Woof Woof")
