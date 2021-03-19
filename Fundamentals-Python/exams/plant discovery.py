n = int(input())
plants = {}

for _ in range(n):
    plant, rarity = input().split("<->")
    plants[plant] = {"rarity": int(rarity), "rating": []}

error = False
command = input()
while command != "Exhibition":
    if ": " not in command:
        error = True
    else:
        command = command.split(": ")
        if command[0] not in ["Rate", "Update", "Reset"]:
            error = True
        else:
            if command[0] == "Reset" and command[1] in plants:
                plants[command[1]]["rating"] = []
            elif command[0] == "Rate":
                if " - " in command[1]:
                    action = command[1].split(" - ")
                    if len(action) == 2 and action[0] in plants and action[1].isdigit():
                        plants[action[0]]["rating"].append(int(action[1]))
                    else:
                        error = True
                else:
                    error = True
            elif command[0] == "Update":
                if " - " in command[1]:
                    action = command[1].split(" - ")
                    if len(action) == 2 and action[0] in plants and action[1].isdigit():
                        plants[action[0]]["rarity"] = int(action[1])
                    else:
                        error = True
                else:
                    error = True
            else:
                error = True
    if error:
        print("error")
        error = False
    command = input()

for pl in plants:
    if plants[pl]["rating"]:
        plants[pl]["rating"] = sum(plants[pl]["rating"]) / len(plants[pl]["rating"])
    else:
        plants[pl]["rating"] = 0

print("Plants for the exhibition:")
for pl, atrib in sorted(plants.items(), key=lambda x: (-x[1]["rarity"], -x[1]["rating"])):
    print(f"- {pl}; Rarity: {atrib['rarity']}; Rating: {atrib['rating']:.2f}")
