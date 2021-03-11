n = int(input())
army = {}

for _ in range(n):
    tipe, name, damage, health, armor = input().split()
    if damage == 'null':
        damage = 45
    damage = int(damage)
    if health == 'null':
        health = 250
    health = int(health)
    if armor == 'null':
        armor = 10
    armor = int(armor)
    dragon = {name: [damage, health, armor]}
    if tipe not in army:
        army[tipe] = dict(dragon)
    else:
        valid = False
        for k, n in army[tipe].items():
            if name == k:
                army[tipe][k] = [damage, health, armor]
                valid = True
                break
        if not valid:
            army[tipe].update(dragon)

for ti, na in army.items():
    print(f'{ti}::({sum(x[0] for x in na.values()) / len(na):.2f}/{sum(x[1] for x in na.values()) / len(na):.2f}/{sum(x[2] for x in na.values()) / len(na):.2f})')
    for c, v in sorted(na.items()):
        print(f'-{c} -> damage: {v[0]}, health: {v[1]}, armor: {v[2]}')
