gifts = input()
gifts = gifts.split(' ')
command = input()
while command != 'No Money':
    command = command.split(' ')
    if command[0] == 'OutOfStock':
        for i in range(len(gifts)):
            if gifts[i] == command[1]:
                gifts[i] = 'None'
    elif command[0] == 'Required' and int(command[2]) < len(gifts):
        gifts[int(command[2])] = command[1]
    elif command[0] == 'JustInCase':
        gifts[-1] = command[1]
    result = gifts
    command = input()
for r in result:
    if r == 'None':
        result.remove('None')
result = ' '.join(result)
print(result)
