numbers = [int(x) for x in input().split(' ')]
command = input()

while command != 'end':
    command = command.split(' ')
    if command[0] == 'swap':
        ind1 = int(command[1])
        ind2 = int(command[2])
        numbers[ind1], numbers[ind2] = numbers[ind2], numbers[ind1]
    elif command[0] == 'multiply':
        ind1 = int(command[1])
        ind2 = int(command[2])
        numbers[ind1] = numbers[ind1] * numbers[ind2]
    elif command[0] == 'decrease':
        numbers = [x-1 for x in numbers]
    command = input()

print(', '.join([str(x) for x in numbers]))
