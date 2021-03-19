n = int(input())
autos = {}

for _ in range(n):
    car, mileage, fuel = input().split("|")
    autos[car] = [int(mileage), int(fuel)]

command = input()
while command != "Stop":
    command = command.split(" : ")
    action = command[0]
    car = command[1]
    if action == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if fuel <= autos[car][1]:
            autos[car][1] -= fuel
            autos[car][0] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")
        if autos[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            autos.pop(car)
    if action == "Refuel":
        fuel = int(command[2])
        autos[car][1] += fuel
        if autos[car][1] > 75:
            print(f"{car} refueled with {fuel - (autos[car][1] - 75)} liters")
            autos[car][1] = 75
        else:
            print(f"{car} refueled with {fuel} liters")
    if action == "Revert":
        kilometers = int(command[2])
        autos[car][0] -= kilometers
        if autos[car][0] < 10000:
            autos[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")
    command = input()

for k, v in sorted(autos.items(),key=lambda x: (-x[1][0], x[0])):
    print(f"{k} -> Mileage: {v[0]} kms, Fuel in the tank: {v[1]} lt.")
