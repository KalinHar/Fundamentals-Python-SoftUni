line = input()
command = input()

while command != "Decode":
    command = command.split("|")
    if command[0] == "Move":
        n = int(command[1])
        line = line[n:] + line[:n]
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        line = line[:index] + value + line[index:]
    elif command[0] == "ChangeAll":
        substr = command[1]
        replacement = command[2]
        line = line.replace(substr, replacement)
    command = input()

print(f"The decrypted message is: {line}")
