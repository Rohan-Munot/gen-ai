# lists: this is mutable

ingredients = ['salt', 'pepper', 'cumin', 'turmeric']
print(f"ingredients: {ingredients}")

spice_options = ['cardamom', 'coriander', 'clove']
ingredients.extend(spice_options)
print(f"ingredients: {ingredients}")
spice_options[0] = 'salt'
print(f"spice_options: {spice_options}")

last_ingredient = ingredients.pop()
print(f"last_ingredient: {last_ingredient}")

raw_byte_array = bytearray(b"ingredients")
new_raw = raw_byte_array.replace(b'ingr', b"tea")
print(f"raw_byte_array: {new_raw}")