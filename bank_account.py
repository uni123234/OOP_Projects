"""
bank_account.py

This module contains the BankAccount class, which is used to represent a bank account
with attributes like name, balance, and passport information. The class provides
methods to get and set these attributes with appropriate validation.
"""


class BankAccount:
    """
    A class to represent a bank account.

    Attributes:
    ----------
    name : str
        Name of the account holder
    balance : float
        Current balance of the account
    passport : str
        Passport information of the account holder (privately stored)
    """

    def __init__(self, name: str, balance: float, passport: str):
        """
        Initializes the BankAccount with a name, balance, and passport information.

        Parameters:
        ----------
        name : str
            Name of the account holder
        balance : float
            Initial balance of the account
        passport : str
            Passport information of the account holder
        """
        self._name = name
        self._balance = balance
        self._passport = passport

    @property
    def name(self) -> str:
        """Get the account holder's name."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Set the account holder's name."""
        if value:
            self._name = value
        else:
            raise ValueError("Name cannot be empty.")

    @property
    def balance(self) -> float:
        """Get the account balance."""
        return self._balance

    @balance.setter
    def balance(self, value: float):
        """Set the account balance."""
        if value >= 0:
            self._balance = value
        else:
            raise ValueError("Balance cannot be negative.")

    @property
    def passport(self) -> str:
        """Get the passport information."""
        return self._passport

    @passport.setter
    def passport(self, value: str):
        """Set the passport information."""
        if value:
            self._passport = value
        else:
            raise ValueError("Passport cannot be empty.")
