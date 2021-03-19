line = input()
command = input()

while command != "Travel":
    command = command.split(":")
    action = command[0]
    if action == "Add Stop":
        index = int(command[1])
        string = command[2]
        if index in range(len(line)):
            line = line[:index] + string + line[index:]
        print(line)
    elif action == "Remove Stop":
        start_ind = int(command[1])
        end_ind = int(command[2])
        if 0 <= start_ind <= end_ind < len(line):
            line = line[:start_ind] + line[end_ind + 1:]
        print(line)
    elif action == "Switch":
        old_str = command[1]
        new_str = command[2]
        if old_str in line:
            line = line.replace(old_str, new_str)
            print(line)
    command = input()

print(f"Ready for world tour! Planned stops: {line}")
