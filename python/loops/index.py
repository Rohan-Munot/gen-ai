# enumerate
menu = ['coffee', 'tea', 'juice', 'water', 'soda']
for idx, item in enumerate(menu, start=1):
    print(f"{idx}. {item}")

# zip: zip is used to combine two lists into a single list of tuples
names = ['ram', 'shyam', 'hari']
ages = [20, 21, 22]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")


# while loop
temp = 40
while temp < 100:
    print(f"temp: {temp}")
    temp += 15
print("temp is greater than 100")

# break, skip, continue
flavours = ['vanilla', 'chocolate', 'strawberry', 'mint', 'coffee']
for flavour in flavours:
    if flavour == 'mint':
        continue
    if flavour == 'coffee':
        print(f"discontinued flavour: {flavour}")
        break

print("loop ended")