class Product:
    """
    A class to represent a food product with nutritional information.

    Attributes:
        name (str): The name of the product.
        calories (float): The number of calories per 100g of the product.
        protein (float): The amount of protein per 100g of the product.
        fat (float): The amount of fat per 100g of the product.
        carbs (float): The amount of carbohydrates per 100g of the product.
    """

    def __init__(self, name, calories, protein, fat, carbs):
        """
        Initialize a new Product instance.

        Args:
            name (str): The name of the product.
            calories (float): The number of calories per 100g.
            protein (float): The amount of protein per 100g.
            fat (float): The amount of fat per 100g.
            carbs (float): The amount of carbohydrates per 100g.
        """
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs


class Meal:
    """
    A class to represent a meal, which consists of multiple food products.

    Attributes:
        products (list): A list of tuples, each containing a Product and its weight in grams.
    """

    def __init__(self):
        """Initialize a new Meal instance with an empty list of products."""
        self.products = []

    def add_product(self, product, weight):
        """
        Add a product to the meal.

        Args:
            product (Product): The product to add to the meal.
            weight (float): The weight of the product in grams.
        """
        self.products.append((product, weight))

    def total_calories(self):
        """
        Calculate the total calories of the meal based on the products and their weights.

        Returns:
            float: The total number of calories in the meal.
        """
        total_calories = 0
        for product, weight in self.products:
            total_calories += (product.calories / 100) * weight
        return total_calories

    def print_meal(self):
        """Print the composition of the meal."""
        print("Meal composition:")
        for product, weight in self.products:
            print(f"{product.name}: {weight}g")
