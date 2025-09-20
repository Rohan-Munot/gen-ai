class Coffee:
    origin = 'Ethiopia'

print(Coffee.origin)

Coffee.roast_level = 'light'
print(Coffee.roast_level)

# creating objects from class Coffee
latte = Coffee()
print(f"latte.origin: {latte.origin}")
print(f"latte.roast_level: {latte.roast_level}")

latte.roast_level = 'medium'
print(f"Class Coffee.roast_level: {Coffee.roast_level}") # class attribute is not changed, namespace, only the property for the object is changed
print(f"latte.roast_level changed: {latte.roast_level}")
