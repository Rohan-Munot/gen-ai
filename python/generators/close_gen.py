# yield from and close
def serve_coffee():
    yield "Coffee: Americano"
    yield "Coffee: Espresso"

def serve_tea():
    yield "Tea: Masala Tea"
    yield "Tea: Green Tea"


def menu():
    yield from serve_coffee()
    yield from serve_tea()

for item in menu():
    print(item)


def shop():
    try:
        while True:
            order = yield "Waiting for menu"
    except:
        print("Shop closed")

stall = shop()
print(next(stall))
stall.close() # this will close the generator cleanup function 