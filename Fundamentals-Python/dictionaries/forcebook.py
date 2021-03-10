line = input()
sides = {}
while line != 'Lumpawaroo':
    if '|' in line:
        line = line.split(' | ')
        name = line[0]
        member = line[1]
        if name not in sides:
            sides[name] = []
        no_exist = True
        for s in sides:
            if member in sides[s]:
                no_exist = False
        if no_exist:
            sides[name].append(member)
    elif ' -> ' in line:
        line = line.split(' -> ')
        name = line[1]
        member = line[0]
        for s in sides:
            if member in sides[s]:
                sides[s].remove(member)
        sides[name].append(member)
        print(f'{member} joins the {name} side!')
    line = input()
sides = dict(reversed(sorted(sides.items())))
sides = dict(reversed(sorted(sides.items(), key=lambda x: len(x[1]))))
for s in sides:
    if len(sides[s]) > 0:
        print(f'Side: {s}, Members: {len(sides[s])}')
        sides[s].sort()
        for m in sides[s]:
            print(f'! {m}')
