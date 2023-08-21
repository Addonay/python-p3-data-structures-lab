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

def get_names(spicy_foods):
    names = [food['name'] for food in spicy_foods]
    return names
food_names = get_names(spicy_foods)
print(food_names)

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food['heat_level'] > 5]
    return spiciest_foods
spiciest_foods = get_spiciest_foods(spicy_foods)
print(spiciest_foods)

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, target_cuisine):
    for food in spicy_foods:
        if food['cuisine'].lower() == target_cuisine.lower():
            return food
    return None
target_cuisine = "Thai"
spicy_food = get_spicy_food_by_cuisine(spicy_foods, target_cuisine)
if spicy_food:
    print(spicy_food)
else:
    print(f"No spicy food found with {target_cuisine} cuisine.")

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)
print_spiciest_foods(spicy_foods)

def average_heat_level(spicy_foods):
    total_heat_level = sum(food['heat_level'] for food in spicy_foods)
    num_foods = len(spicy_foods)
    
    if num_foods == 0:
        return 0
    
    average = total_heat_level / num_foods
    return average
avg_heat = average_heat_level(spicy_foods)
print(f"Average Heat Level: {avg_heat:.2f}")

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)

    return spicy_foods

spicy_food = {
    "name": "Spicy Ramen",
    "cuisine": "Japanese",
    "heat_level": 7,
}
create_spicy_food(spicy_foods, spicy_food)
print(spicy_foods)

