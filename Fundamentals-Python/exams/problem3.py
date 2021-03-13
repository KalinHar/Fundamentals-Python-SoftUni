messages = []
command = input()

while command != "end":
    command = command.split(" ")
    action = command[0]
    if action == "Chat":
        messages.append(command[1])
    if action == "Delete":
        if command[1] in messages:
            messages.remove(command[1])
    if action == "Edit":
        if command[1] in messages:
            for ind, msg in enumerate(messages):
                if msg == command[1]:
                    messages[ind] = command[2]
    if action == "Pin":
        if command[1] in messages:
            messages.remove(command[1])
            messages.append(command[1])
    if action == "Spam":
        spamed = command[1:]
        messages.extend(spamed)
    command = input()

print(*messages, sep="\n")
