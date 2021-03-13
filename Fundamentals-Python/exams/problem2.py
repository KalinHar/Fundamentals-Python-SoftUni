names = input().split(", ")
command = input()
blacklisted = 0
loosed = 0

while command != "Report":
    command = command.split(" ")
    if command[0] == "Blacklist":
        if command[1] not in names:
            print(f"{command[1]} was not found.")
        else:
            for ind, name in enumerate(names):
                if name == command[1]:
                    names[ind] = "Blacklisted"
                    print(f"{name} was blacklisted.")
                    blacklisted += 1
    elif command[0] == "Error":
        index = int(command[1])
        if names[index] not in "Blacklisted Lost":
            print(f"{names[index]} was lost due to an error.")
            names[index] = "Lost"
            loosed += 1
    elif command[0] == "Change":
        index = int(command[1])
        new_name = command[2]
        if 0 <= index < len(names):
            print(f"{names[index]} changed his username to {new_name}.")
            names[index] = new_name
    command = input()

print(f"Blacklisted names: {blacklisted}")
print(f"Lost names: {loosed}")
print(" ".join(names))
