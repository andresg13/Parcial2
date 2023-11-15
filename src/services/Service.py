
from typing import List, Optional

from models.client import Client
from models.factory import Factory


class Service:

    def __init__(self, max_clients: int) -> None:
        self.max_clients = max_clients
        self.clients = []

    def add_client(self, client: Client) -> None:
        if len(self.clients) >= self.max_clients:
            raise Exception("Max clients reached")

        self.clients.append(client)

    def factories_summary(self) -> None:
        factory_types_count = {}
        for client in self.clients:
            factory_type = client.factory_type
            if factory_type not in factory_types_count:
                factory_types_count[factory_type] = 0

            factory_types_count[factory_type] += 1

        for factory_type, count in factory_types_count.items():
            print(f'{factory_type} factory: {count} clients')

    def client_most_expensive_food(self) -> tuple[int, str, float]:
        client_id = None
        food_type = None
        food_cost = None

        for client in self.clients:
            food = client.comsuption.make_food()
            if food_cost is None or food.cost > food_cost:
                client_id = client.id
                food_type = food.type
                food_cost = food.cost

        return client_id, food_type, food_cost
