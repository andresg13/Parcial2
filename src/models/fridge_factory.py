from models.factory import Factory


class FridgeFactory(Factory):

    def __init__(self) -> None:
        super().__init__()
        self.make_food_type = lambda: 'beet'

    def make_appliance(self, model_number: int, consumption: str, weight: float, cost: float) -> appliance:
        return Fridge(model_number, consumption, weight, cost)
