command = input()
towns = []
while command != 'Sail':
    command = command.split('||')
    for i in range(1, len(command)):
        command[i] = int(command[i])
    town = True
    for t in towns:
        if command[0] in t:
            t[1] += command[1]
            t[2] += command[2]
            town = False
            break
    if town:
        towns.append(command)
    command = input()
action = input()
while action != "End":
    action = action.split('=>')
    for i in range(2, len(action)):
        action[i] = int(action[i])
    if action[0] == 'Plunder':
        for t in towns:
            if action[1] == t[0]:
                t[1] -= int(action[2])
                if t[1] < 0:
                    action[2]  += t[1]
                t[2] -= action[3]
                if t[2] < 0:
                    action[3] += t[2]
                print(f'{t[0]} plundered! {action[3]} gold stolen, {action[2]} citizens killed.')
                if t[1] <= 0 or t[2] <= 0:
                    print(f'{t[0]} has been wiped off the map!')
                    towns.remove(t)
                    break
    elif action[0] == 'Prosper':
        if action[2] < 0:
            print('Gold added cannot be a negative number!')
        else:
            for t in towns:
                if action[1] == t[0]:
                    t[2] += action[2]
                    print(f'{action[2]} gold added to the city treasury. {t[0]} now has {t[2]} gold.')
    action = input()
if len(towns) >= 1:
    print(f'Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:')
    # towns.sort(key = lambda x: x[1])
    # towns.sort(key = lambda x: x[2])
    # towns.reverse()
    for t in reversed(sorted(towns, key=lambda x: (x[2], x[1]))):
        print(f'{t[0]} -> Population: {t[1]} citizens, Gold: {t[2]} kg')
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')

