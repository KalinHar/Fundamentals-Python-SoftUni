targets = [int(x) for x in (input().split(' '))]
command =input()

while command != 'End':
    command = command.split(' ')
    action = command[0]
    index = int(command[1])
    value = int(command[2])
    if action == 'Shoot':
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.remove(targets[index])
    elif action == 'Add':
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print('Invalid placement!')
    elif action == 'Strike':
        if index - value < 0 or index + value >= len(targets):
            print('Strike missed!')
        else:
            targets = targets[:index-value] + targets[index+value+1:]
    command = input()
print('|'.join([str(x) for x in targets]))
