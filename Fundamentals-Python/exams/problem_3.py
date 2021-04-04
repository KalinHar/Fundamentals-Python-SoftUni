unliked = 0
guests = {}
command = input()

while command != "Stop":
    action, name, meal = command.split("-")
    if action == "Like":
        if name not in guests:
            guests[name] = {"meal": [meal]}
        else:
            if meal not in guests[name]['meal']:
                guests[name]['meal'].append(meal)
    elif action == "Unlike":
        if name not in guests:
            print(f"{name} is not at the party.")
        else:
            if meal not in guests[name]['meal']:
                print(f"{name} doesn't have the {meal} in his/her collection.")
            else:
                guests[name]['meal'].remove(meal)
                print(f"{name} doesn't like the {meal}.")
                unliked += 1
    command = input()

for guest, arg in sorted(guests.items(), key=lambda x: (-len(x[1]["meal"]), x[0])):
    print(f"{guest}: {(', '.join(arg['meal']))}")
print(f"Unliked meals: {unliked}")
