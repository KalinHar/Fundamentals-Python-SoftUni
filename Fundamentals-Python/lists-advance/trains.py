n = int(input())
train = [0] * n
command = input()
while command != 'End':
    command = command.split(' ')
    if command[0] == "add":
        train[-1] += int(command[1])
    elif command[0] == "insert":
        vag = int(command[1])
        peo = int(command[2])
        train[vag] += peo
    elif command[0] == "leave":
        vag = int(command[1])
        peo = int(command[2])
        train[vag] -= peo
    command = input()
print(train)
