targets = [int(x) for x in input().split(' ')]
action = input()
while action != "End":
    action = action.split(' ')
    index = int(action[1])
    value = int(action[2])
    if action[0] == 'Shoot':
        if index < 0 or index > len(targets) - 1:
            action = input()
        else:
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)
            action = input()
    elif action[0] == 'Add':
        if index < 0 or index > len(targets) - 1:
            print('Invalid placement!')
            action = input()
        else:
            targets.insert(index, value)
            action = input()
    elif action[0] == 'Strike':
        if index - value < 0 or index + value > len(targets) - 1:
            print('Strike missed!')
            action = input()
        else:
            targets = targets[:index - value] + targets[index + value +1:]
            action = input()
targets = [str(x) for x in targets]
print('|'.join(targets))
