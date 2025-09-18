# dictionary: this is mutable
# member ship test can be done here and in the list

soft_drink = dict(name="Coca-Cola", price=10, quantity=10)
print(f"soft_drink: {soft_drink}")
del soft_drink['quantity']
print(f"soft_drink: {soft_drink}")

recipe = {}
recipe['name'] = 'Coca-Cola'
recipe['sweetener'] = 'sugar'
recipe['quantity'] = 10

print(f"recipe: {recipe['name']}")