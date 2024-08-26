"""
car.py

This module contains the Car class, which is used to represent a car with attributes
like brand, model, and year of manufacture. The class also provides a string
representation of the car.
"""

class Car:
    """
    A class to represent a car.

    Attributes:
    ----------
    brand : str
        The brand of the car
    model : str
        The model of the car
    year : int
        The year the car was manufactured
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Initializes the Car with a brand, model, and year of manufacture.

        Parameters:
        ----------
        brand : str
            The brand of the car
        model : str
            The model of the car
        year : int
            The year the car was manufactured
        """
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """
        Returns a string representation of the car.

        Returns:
        -------
        str
            A formatted string describing the car's brand, model, and year of manufacture.
        """
        return f"My car is {self.brand}. Model - {self.model}. Created in {self.year}"
