class ServingSize:
    size = 180

    def describe(self):
        return f"The serving size is {self.size}ml"


coffeeCup = ServingSize()
print(coffeeCup.describe())

coffeeCup_two = ServingSize()
coffeeCup_two.size = 200
print(coffeeCup_two.describe())
print(ServingSize.describe(coffeeCup_two))