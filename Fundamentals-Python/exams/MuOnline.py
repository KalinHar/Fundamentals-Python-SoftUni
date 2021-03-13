game = input()
monster = ''
points = ''
health = 100
bitcoin = 0
rooms = 0
count = 0
flag = True
for s in game:
    count += 1
    if s == ' ':
        flag = False
        continue
    elif s == '|' or count == len(game):
        if count == len(game):
            points += s
        rooms += 1
        if monster == 'potion':
            health += int(points)
            if health > 100:
                amount = int(points) - int(health % 100)
                health = 100
            else:
                amount = int(points)
            print(f'You healed for {amount} hp.')
            print(f'Current health: {health} hp.')
        elif monster == 'chest':
            bitcoin += int(points)
            print(f'You found {points} bitcoins.')
        else:
            health -= int(points)
            if health <= 0:
                print(f'You died! Killed by {monster}.')
                print(f'Best room: {rooms}')
                break
            else:
                print(f'You slayed {monster}.')
        monster = ''
        points = ''
        flag = True
        continue
    if flag:
        monster += s
    else:
        points += s
if health > 0:
    print("You've made it!")
    print(f'Bitcoins: {bitcoin}')
    print(f'Health: {health}')
