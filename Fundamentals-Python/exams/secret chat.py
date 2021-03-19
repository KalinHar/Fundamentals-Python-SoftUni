message = input()
command = input()

while command != "Reveal":
    command = command.split(":|:")
    action = command[0]
    if action == "InsertSpace":
        index = int(command[1])
        message = message[:index] + " " + message[index:]
        print(message)
    elif action == "Reverse":
        substr = command[1]
        if substr in message:
            message = message.replace(substr, "", 1)
            message += substr[::-1]
            print(message)
        else:
            print("error")
    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)
        print(message)
    command = input()

print(f"You have a new text message: {message}")
