n = int(input())
heroes = {}

for _ in range(n):
    name, hp, mp = input().split()
    hp = int(hp)
    mp = int(mp)
    heroes[name] = [hp, mp]

command = input()
while command != "End":
    command = command.split(" - ")
    action = command[0]
    hero = command[1]
    if action == "CastSpell":
        mp_need = int(command[2])
        spell_name = command[3]
        if mp_need <= heroes[hero][1]:
            heroes[hero][1] -= mp_need
            print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero][1]} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        if damage >= heroes[hero][0]:
            heroes.pop(hero)
            print(f"{hero} has been killed by {attacker}!")
        else:
            heroes[hero][0] -= damage
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero][0]} HP left!")
    elif action == "Recharge":
        amount = int(command[2])
        heroes[hero][1] += amount
        if heroes[hero][1] > 200:
            amount = 200 - (heroes[hero][1] - amount)
            heroes[hero][1] = 200
        print(f"{hero} recharged for {amount} MP!")
    elif action == "Heal":
        amount = int(command[2])
        heroes[hero][0] += amount
        if heroes[hero][0] > 100:
            amount = 100 - (heroes[hero][0] - amount)
            heroes[hero][0] = 100
        print(f"{hero} healed for {amount} HP!")
    command = input()

for he, power in sorted(heroes.items(), key=lambda x: (-x[1][0], x[0])):
    print(f"{he}\n  HP: {power[0]}\n  MP: {power[1]}")
