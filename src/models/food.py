from typing import Optional


class Food:

    def __init__(self, type: str, cost: float) -> None:
        self.type = type
        self.cost = cost

    def __str__(self) -> str:
        return f'{self.type} food with cost {self.cost}'

