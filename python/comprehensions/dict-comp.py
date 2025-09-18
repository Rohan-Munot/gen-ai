menu_prices = {
    "coffee": 10,
    "tea": 5,
    "juice": 15,
    "water": 20,
    "mango soda": 25,
}

prices_with_tax = {menu_item: price * 1.1 for menu_item, price in menu_prices.items()}
print(f"prices_with_tax: {prices_with_tax}")