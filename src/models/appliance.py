from typing import Optional


class Appliance:

    def __init__(self, model_number: int, consumption: str, weight: float, cost: float) -> None:
        self.model_number = model_number
        self.consumption = consumption
        self.weight = weight
        self.cost = cost

    def make_food(self) -> Optional["food"]:

        if self.factory_type is None:
            return None

        food_type = self.factory_type.make_food_type()
        if food_type is None:
            return None

        return Food(food_type, self.cost)
