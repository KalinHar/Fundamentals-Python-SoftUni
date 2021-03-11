text = input().split('|')
energy = 100
coins = 100
for event in text:
    task, bonus = event.split('-')
    bonus = int(bonus)
    if task == 'rest':
        energy += bonus
        if energy > 100:
            bonus = bonus - (energy - 100)
            energy = 100
        print(f'You gained {bonus} energy.')
        print(f'Current energy: {energy}.')
    elif task == 'order':
        if energy >= 30:
            coins += bonus
            energy -= 30
            print(f'You earned {bonus} coins.')
        else:
            energy += 50
            if energy > 100:
                energy = 100
            print('You had to rest!')
    else:
        if coins > bonus:
            coins -= bonus
            print(f'You bought {task}.')
        else:
            coins -= bonus
            print(f'Closed! Cannot afford {task}.')
            break
if coins > 0:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
