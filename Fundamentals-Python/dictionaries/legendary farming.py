line = input().split(' ')
legend = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
legendary = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
winner = None
while not winner:
    for ind in range(0, len(line), 2):
        material = line[ind + 1].lower()
        if material in legendary:
            legendary[material] += int(line[ind])
            if legendary[material] >= 250:
                legendary[material] -= 250
                winner = material
                break
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += int(line[ind])
    if winner:
        break
    line = input().split(' ')
print(f'{legend[winner]} obtained!')
for m, q in sorted(legendary.items(), key=lambda  kvp: (-kvp[1], kvp[0])):
    print(f'{m}: {q}')
for t, j in sorted(junk.items()):
    print(f'{t}: {j}')
