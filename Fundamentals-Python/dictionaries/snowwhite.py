command = input()
dwarfs = {}

while command != 'Once upon a time':
    name, color, physics = command.split(' <:> ')
    if color not in dwarfs:
        dwarfs[color] = {name: physics}
    else:
        if name not in dwarfs[color]:
            dwarfs[color].update({name: physics})
        else:
        dwarfs.update({name_colour : int(physics)})
    command = input()

masive = []
for dcn, ph in dwarfs.items():
    co, na = dcn.split(' ')
    masive.append([ph, co, na])
new_masive = list(reversed(sorted(masive)))
print(masive)
print(new_masive)

# Pesho <:> Red <:> 2000
# Tosho <:> Blue <:> 1000
# Gosho <:> Green <:> 1000
# Tosho <:> Grey <:> 233
# Tosho <:> Grey <:> 23
# Tosho <:> Red <:> 23
# Sasho <:> Yellow <:> 4500
# Prakasho <:> Stamat <:> 1000
# Once upon a time
