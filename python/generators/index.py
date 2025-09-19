# generators are used to create iterators to get one element 
# tou save memory
# lazy evaluation
#  you dont want results immediately

def serve_coffee():
    yield "Coffee: Americano"
    yield "Coffee: Espresso"
    yield "Coffee: Latte"
stall = serve_coffee()

for coffee in stall:
    print(coffee)

print(next(stall))
print(next(stall))
print(next(stall))
# print(next(stall)) # this will raise StopIteration error
