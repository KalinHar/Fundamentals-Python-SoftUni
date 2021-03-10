line = input()
companies = {}
while line != 'End':
    line = line.split(' -> ')
    name = line[0]
    ide = line[1]
    if name not in companies:
        companies[name] = [ide]
    else:
        if ide not in companies[name]:
            companies[name].append(ide)
    line = input()
companies = dict(sorted(companies.items()))
for c in companies:
    print(c)
    for i in companies[c]:
        print(f'-- {i}')
