# tuples: this is immutable

spices = ('cardamom', 'pepper', 'cumin', 'turmeric')

( spice1, spice2, spice3, spice4 ) = spices
print(f"spice1: {spice1}, spice2: {spice2}, spice3: {spice3}, spice4: {spice4}")

# usecase
pepper_ratio, cumin_ratio = 2,1
print(f"Ratio of pepper: {pepper_ratio} and cumin: {cumin_ratio}")
pepper_ratio, cumin_ratio = cumin_ratio, pepper_ratio
print(f"Ratio of pepper: {pepper_ratio} and cumin: {cumin_ratio}")

# membership test
print(f"'cardamom' in spices: {'cardamom'in spices}")
print(f"'cardamom' not in spices: {'cardamom' not in spices}")