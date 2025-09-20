class Coffee:
    temperature = 'hot'
    roast_level = 'light'

latte = Coffee()
print(f"latte.temperature: {latte.temperature}")

latte.temperature = 'cold'
# adding new prop
latte.size = 'large'
print(f"latte.temperature_changed: {latte.temperature}")
print(f"latte.size: {latte.size}")
print(f"Coffee.temperature: {Coffee.temperature}")

del latte.temperature
del latte.size
print(f"after deletion: {latte.temperature}") # this will not raise an error because the attribute is defined in class, this is called attribute shadowing
print(f"after deletion: {latte.size}") # this will raise an error because the attribute is not defined in the class

# The fallback is called attribute shadowing