"""
main.py

This module provides examples of using various classes including User, Car, 
and characters in a game (Archer, Wizard, Knight), as well as Meal and Product 
classes for meal management.
"""

from user import User
from hero import Archer, Wizard, Knight
from car import Car
from meal import Product, Meal

def main():
    """
    Main function to demonstrate the functionality of different classes.
    """
    # Example with User
    user1 = User("Oleg", "Nin", 44)
    user1.print_info()

    # Example with Car
    my_car = Car("Toyota", "Corolla", 2022)
    print(my_car)

    # Example with Game
    print("Welcome to the game!")
    # Removed the unused 'name' variable
    hero = None
    while hero is None:
        try:
            answer = int(input("Choose your role\n 1:Archer 2:Knight 3:Wizard\n"))
            if answer == 1:
                hero = Archer(1)
            elif answer == 2:
                hero = Knight(1)
            elif answer == 3:
                hero = Wizard(1)
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Please enter a number.")

    print(hero)

    enemy1 = Knight(1)
    print(f"Your enemy is {enemy1} \nHp is {enemy1.hp}")

    for _ in range(3):
        enemy1.hp -= hero.attack_func()
        enemy1.hell_check()

    print(f"Your enemy is {enemy1} \nHp is {enemy1.hp}")

    # Example with Meal
    apple = Product("Apple", 52, 0.3, 0.2, 14)
    rice = Product("Rice", 130, 2.7, 0.3, 28)
    chicken_breast = Product("Chicken Breast", 165, 31, 3.6, 0)

    meal = Meal()
    meal.add_product(apple, 150)
    meal.add_product(rice, 200)
    meal.add_product(chicken_breast, 250)

    meal.print_meal()
    print(f"Total calories: {meal.total_calories()} kcal")

if __name__ == "__main__":
    main()
