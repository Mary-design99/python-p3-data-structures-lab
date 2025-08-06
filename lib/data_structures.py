# The list of dictionaries representing different spicy foods
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(foods):
    """
    Returns a list of the names of each spicy food using a list comprehension.
    """
    return [food['name'] for food in foods]

def get_spiciest_foods(foods):
    """
    Returns a list of dictionaries for foods with a heat level greater than 5.
    """
    return [food for food in foods if food['heat_level'] > 5]

def print_spicy_foods(foods):
    """
    Outputs each spicy food to the terminal in a specific format.
    """
    for food in foods:
        heat_level_emojis = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def get_spicy_food_by_cuisine(foods, cuisine):
    """
    Returns a single dictionary for the food whose cuisine matches the input string.
    """
    for food in foods:
        if food['cuisine'] == cuisine:
            return food
    return None # Return None if no match is found

def print_spiciest_foods(foods):
    """
    Outputs only the spiciest foods (heat level > 5) in the specified format.
    This function reuses get_spiciest_foods() and print_spicy_foods().
    """
    spiciest_foods_list = get_spiciest_foods(foods)
    print_spicy_foods(spiciest_foods_list)

def get_average_heat_level(foods):
    """
    Returns the average heat level of all spicy foods.
    """
    total_heat = sum(food['heat_level'] for food in foods)
    return int(total_heat / len(foods))

def create_spicy_food(foods, new_food):
    """
    Returns the original list with a new spicy food dictionary added to it.
    """
    foods.append(new_food)
    return foods

# Example function calls to demonstrate the code works
if __name__ == "__main__":
    print("--- Testing get_names() ---")
    print(get_names(spicy_foods))

    print("\n--- Testing get_spiciest_foods() ---")
    print(get_spiciest_foods(spicy_foods))

    print("\n--- Testing print_spicy_foods() ---")
    print_spicy_foods(spicy_foods)

    print("\n--- Testing get_spicy_food_by_cuisine('American') ---")
    print(get_spicy_food_by_cuisine(spicy_foods, "American"))

    print("\n--- Testing print_spiciest_foods() ---")
    print_spiciest_foods(spicy_foods)

    print("\n--- Testing get_average_heat_level() ---")
    print(get_average_heat_level(spicy_foods))

    print("\n--- Testing create_spicy_food() ---")
    new_food = {'name': 'Griot', 'cuisine': 'Haitian', 'heat_level': 10}
    updated_foods = create_spicy_food(spicy_foods, new_food)
    print(updated_foods)
