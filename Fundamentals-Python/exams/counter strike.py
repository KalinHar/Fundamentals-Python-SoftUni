energy = int(input())
battles_count = 0
command = input()
no_energy = False

while command != 'End of battle':
    distance = int(command)
    if energy >= distance:
        energy -= distance
        battles_count += 1
        if battles_count % 3 == 0:
            energy += battles_count
    else:
        no_energy = True
        break
    command = input()

if no_energy:
    print(f"Not enough energy! Game ends with {battles_count} won battles and {energy} energy")
else:
    print(f"Won battles: {battles_count}. Energy left: {energy}")
