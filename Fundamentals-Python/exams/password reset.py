password = input()
command = input()
while command != "Done":
    if command == "TakeOdd":
        new_pass = ""
        for i in range(1, len(password), 2):
            new_pass += password[i]
        password = new_pass
        print(password)
        command = input()
        continue
    command = command.split()
    if command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        gets = password[index: index + length]
        password = password.replace(gets, "", 1)
        print(password)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
    command = input()
print(f"Your password is: {password}")
