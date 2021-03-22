command = input()
dwarfs = {}

while command != 'Once upon a time':
    name, color, physics = command.split(' <:> ')
    if color not in dwarfs:
        dwarfs[color] = {name: int(physics)}
    else:
        if name not in dwarfs[color]:
            dwarfs[color].update({name: int(physics)})
        else:
            if int(physics) > dwarfs[color][name]:
                dwarfs[color][name] = int(physics)
    command = input()

sort_dw_by_color = []
for col, name_physics in sorted(dwarfs.items(), key=lambda x: -len(x[1])):
    for dn in name_physics:
        sort_dw_by_color.append([dn, col, name_physics[dn]])

for dwarf in sorted(sort_dw_by_color, key=lambda x: -x[2]):
    print(f"({dwarf[1]}) {dwarf[0]} <-> {dwarf[2]}")

