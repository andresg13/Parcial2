def main() -> None:
    service = Service(20)

    factories_types = [2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 1, 2]
    model_numbers = [5, 5, 4, 3, 1, 2, 4, 4, 4, 2, 5, 3, 4, 2, 4, 2, 3, 5, 3, 2, 2]
    consumptions = ['Very High', 'Low', 'Very Low', 'Very High', 'High', 'Medium', 'High', 'Low', 'Medium', 'High', 'Very High', 'Medium', 'Medium', 'Very High', 'Very High', 'Medium', 'Medium', 'Low', 'High', 'Very Low', 'Medium']
    weights = [0.07, 0.21, 1.55, 1.72, 0.35, 0.52, 1.45, 1.78, 0.34, 1.79, 0.49, 0.09, 0.74, 0.87, 1.28, 0.35, 1.08, 0.57, 1.32, 1.89, 1.80]
    costs = [0.13, 43.81, 17.65, 10.16, 2.99, 31.09, 38.97, 16.03, 47.35, 27.31, 35.89, 30.81, 14.33, 13.04, 45.88, 7.74, 44.64, 49.63, 18.93, 39.39, 33.08]
    
    for (factory_type, model_number, consumption, weight, cost) in zip(factories_types, model_numbers, consumptions, weights, costs):
        service.add_client(Client(factory_type, model_number, consumption, weight, cost))

    service.factories_summary()

    client_id, food_type, food_cost = service.client_most_expensive_food()
    print(f'Client\'s {client_id} {food_type} is the most expensive with {food_cost} dollars')


if __name__ == '__main__':
    main()


"""
Service started, waiting for Clients...

Client 1 created
Microwave(5, 'Very High') created
Spaghetti(0.07, 0.13) created
Client 1 added to Service

Client 2 created
Fridge(5, 'Low') created
Beef(0.21, 43.81) created
Client 2 added to Service

Client 3 created
Microwave(4, 'Very Low') created
Spaghetti(1.55, 17.65) created
Client 3 added to Service

Client 4 created
Fridge(3, 'Very High') created
Beef(1.72, 10.16) created
Client 4 added to Service

Client 5 created
Microwave(1, 'High') created
Spaghetti(0.35, 2.99) created
Client 5 added to Service

Client 6 created
Microwave(2, 'Medium') created
Spaghetti(0.52, 31.09) created
Client 6 added to Service

Client 7 created
Microwave(4, 'High') created
Spaghetti(1.45, 38.97) created
Client 7 added to Service

Client 8 created
Microwave(4, 'Low') created
Spaghetti(1.78, 16.03) created
Client 8 added to Service

Client 9 created
Microwave(4, 'Medium') created
Spaghetti(0.34, 47.35) created
Client 9 added to Service

Client 10 created
Microwave(2, 'High') created
Spaghetti(1.79, 27.31) created
Client 10 added to Service

Client 11 created
Fridge(5, 'Very High') created
Beef(0.49, 35.89) created
Client 11 added to Service

Client 12 created
Fridge(3, 'Medium') created
Beef(0.09, 30.81) created
Client 12 added to Service

Client 13 created
Microwave(4, 'Medium') created
Spaghetti(0.74, 14.33) created
Client 13 added to Service

Client 14 created
Fridge(2, 'Very High') created
Beef(0.87, 13.04) created
Client 14 added to Service

Client 15 created
Fridge(4, 'Very High') created
Beef(1.28, 45.88) created
Client 15 added to Service

Client 16 created
Fridge(2, 'Medium') created
Beef(0.35, 7.74) created
Client 16 added to Service

Client 17 created
Microwave(3, 'Medium') created
Spaghetti(1.08, 44.64) created
Client 17 added to Service

Client 18 created
Microwave(5, 'Low') created
Spaghetti(0.57, 49.63) created
Client 18 added to Service

Client 19 created
Fridge(3, 'High') created
Beef(1.32, 18.93) created
Client 19 added to Service

Client 20 created
Fridge(2, 'Very Low') created
Beef(1.89, 39.39) created
Client 20 added to Service

Client 21 created
Microwave(2, 'Medium') created
Spaghetti(1.8, 33.08) created
Client limit reached, unable to add new Client

Factories Summary:

- Clients using Factory 1 = 9
- Clients using Factory 2 = 11

- Client 1 uses Factory 2
- Client 2 uses Factory 1
- Client 3 uses Factory 2
- Client 4 uses Factory 1
- Client 5 uses Factory 2
- Client 6 uses Factory 2
- Client 7 uses Factory 2
- Client 8 uses Factory 2
- Client 9 uses Factory 2
- Client 10 uses Factory 2
- Client 11 uses Factory 1
- Client 12 uses Factory 1
- Client 13 uses Factory 2
- Client 14 uses Factory 1
- Client 15 uses Factory 1
- Client 16 uses Factory 1
- Client 17 uses Factory 2
- Client 18 uses Factory 2
- Client 19 uses Factory 1
- Client 20 uses Factory 1

Client's 18 Spaghetti is the most expensive with 49.63 dollars
"""
