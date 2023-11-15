from typing import Optional
from abc import ABC, abstractmethod


class Factory:

    def __init__(self) -> None:
        self.make_food_type = None
        
    @abstractmethod
    def make_appliance(self, model_number: int, consumption: str, weight: float, cost: float) -> "appliance":
        raise NotImplementedError()
