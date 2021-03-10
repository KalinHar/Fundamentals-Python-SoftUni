line = input()
sides = {}
while line != 'Lumpawaroo':
    if '|' in line:
        line = line.split(' | ')
        name = line[0]
        member = line[1]
        no_exist = True
        for s in sides:
            if member in sides[s]:
                no_exist = False
                break
        if no_exist:
            if name not in sides:
                sides[name] = []
            sides[name].append(member)
    elif ' -> ' in line:
        line = line.split(' -> ')
        name = line[1]
        member = line[0]
        for s in sides:
            if member in sides[s]:
                sides[s].remove(member)
                break
        if name not in sides:
            sides[name] = []
        sides[name].append(member)
        print(f'{member} joins the {name} side!')
    line = input()
# sides = dict(reversed(sorted(sides.items())))
# sides = dict(reversed(sorted(sides.items(), key=lambda x: len(x[1]))))
for s in dict(sorted(sides.items(), key=lambda x: (-len(x[1]), x[0]))):
    if len(sides[s]) > 0:
        print(f'Side: {s}, Members: {len(sides[s])}')
        sides[s].sort()
        for m in sides[s]:
            print(f'! {m}')
