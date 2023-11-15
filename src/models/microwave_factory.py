from models.factory import Factory

class MicrowaveFactory(Factory):

    def __init__(self) -> None:
        super().__init__()
        self.make_food_type = lambda: 'spaghetti'

    def make_appliance(self, model_number: int, consumption: str, weight: float, cost: float) -> appliance:
        return Microwave(model_number, consumption, weight, cost)