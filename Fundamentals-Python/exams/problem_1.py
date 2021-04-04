user = input().strip()
command = input()

while not command == "Sign up ":
    command = command.split()
    if command[0] == "Case":
        if command[1] == "lower":
            user = user.lower()
        elif command[1] == "upper":
            user = user.upper()
        print(user)
    elif command[0] == "Reverse":
        start_ind = int(command[1])
        end_ind = int(command[2])
        if 0 <= start_ind <= end_ind < len(user):
            reversed_str = user[start_ind:end_ind+1]
            reversed_str = reversed_str[::-1]
            print(reversed_str)
    elif command[0] == "Cut":
        sub_str = command[1]
        if sub_str in user:
            user = user.replace(sub_str, "")
            print(user)
        else:
            print(f"The word {user} doesn't contain {sub_str}.")
    elif command[0] == "Replace":
        char = command[1]
        user = user.replace(char, "*")
        print(user)
    elif command[0] == "Check":
        v_char = command[1]
        if v_char in user:
            print("Valid")
        else:
            print(f"Your username must contain {v_char}.")
    command = input()

