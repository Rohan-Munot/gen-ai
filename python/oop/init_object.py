class Orders:
    def __init__(self, type_, size) -> None:
        self.type = type_
        self.size = size


    def describe(self):
        return f"The order is {self.type} and the size is {self.size}"


order = Orders("coffee", 180)
print(order.describe())

order_two = Orders("tea", 200)
print(order_two.describe())