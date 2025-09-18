# sets: this is mutable

essential_spices = {'cumin', 'coriander', 'clove'}
optional_spices = {'cardamom', 'clove', 'turmeric'} 

all_spices = essential_spices.union(optional_spices)
print(f"all_spices: {all_spices}")

common_spices = essential_spices.intersection(optional_spices)
print(f"common_spices: {common_spices}")

only_essential_spices = essential_spices.difference(optional_spices)
print(f"only_essential_spices: {only_essential_spices}")
