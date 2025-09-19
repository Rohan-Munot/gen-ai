def customer(): 
    print("Welcome to the coffee shop")
    order = yield
    while True:
        print(f"Order: {order}")
        order = yield

stall = customer()
next(stall) # this will print the welcome message i.e start the generator
stall.send("Coffee: Americano") # this will send the order to the generator
# stall.send("Coffee: Espresso") # this will send the order to the generator
# stall.send("Coffee: Latte") # this will send the order to the generator