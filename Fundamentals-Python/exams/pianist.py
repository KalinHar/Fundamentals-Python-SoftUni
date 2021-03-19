n = int(input())
collection = {}

for _ in range(n):
    piece, composer, key = input().split("|")
    collection[piece] = {"composer": composer, "key": key}

command = input()
while command != "Stop":
    command = command.split("|")
    if command[0] == "Add":
        if command[1] in collection:
            print(f"{command[1]} is already in the collection!")
        else:
            collection[command[1]] = {"composer": command[2], "key": command[3]}
            print(f"{command[1]} by {command[2]} in {command[3]} added to the collection!")
    elif command[0] == "Remove":
        if command[1] in collection:
            collection.pop(command[1])
            print(f"Successfully removed {command[1]}!")
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        if command[1] in collection:
            print(f"Changed the key of {command[1]} to {command[2]}!")
            collection[command[1]]["key"] = command[2]
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")
    command = input()

for p, atr in sorted(collection.items(), key=lambda x: (x, x[1]["composer"])):
    print(f"{p} -> Composer: {atr['composer']}, Key: {atr['key']}")
