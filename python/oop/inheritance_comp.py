class BaseChai:
    def __init__(self, name) -> None:
        self.name = name
    
    def prepare(self):
        print(f"Preparing {self.name}")
    
class MatchaChai(BaseChai):
    def add_spices(self):
        print(f"Adding spices to {self.name}")


class ChaiShop:
    chai_cls = BaseChai

    def __init__(self) -> None:
        self.chai = self.chai_cls("regular")

    def serve(self):
        print(f"Serving {self.chai.name}")
        self.chai.prepare()

class MatchaChaiShop(ChaiShop):
    chai_cls = MatchaChai

shop = ChaiShop()
fancy = MatchaChaiShop()
shop.serve()
fancy.serve()

fancy.chai.add_spices()