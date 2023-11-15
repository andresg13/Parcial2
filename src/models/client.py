from typing import Optional, Type


class Client:

    def __init__(self, id: int, factory_type: Type["factory"], model_number: int, consumption: str, weight: float) -> None:
        self.id = id
        self.factory_type = factory_type
        self.model_number = model_number
        self.consumption = consumption
        self.weight = weight

    def __str__(self) -> str:
        return f'Client {self.id} with factory {self.factory_type}'
