favourites = [
    "coffee",
    "tea",
    "juice",
    "mango soda",
    "mango soda",
    "orange soda",
    "milk",
]
unique_items = {item for item in favourites} # set comprehension removes duplicates
print(f"unique_items: {unique_items}")

recipes = {
    "Masala Tea": ["tea", "milk", "sugar", "masala"],
    "Mango Soda": ["mango", "sugar", "soda"],
    "Coffee": ["coffee", "sugar", "milk"],   
}

unique_ingredients = {ingredient for recipe in recipes.values() for ingredient in recipe}
print(unique_ingredients)