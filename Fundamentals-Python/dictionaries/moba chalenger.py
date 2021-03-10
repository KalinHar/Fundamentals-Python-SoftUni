line = input()
ranglist = {}
while line != 'Season end':
    if '->' in line:
        line = line.split(' -> ')
        player = line[0]
        pos = line[1]
        skill = int(line[2])
        if player not in ranglist:
            ranglist[player] = {pos: skill}
        else:
            if pos not in ranglist[player]:
                ranglist[player].update({pos: skill})
            else:
                if ranglist[player][pos] < skill:
                    ranglist[player][pos] = skill
    else:
        line = line.split(' vs ')
        pl1 = line[0]
        pl2 = line[1]
        if pl1 in ranglist and pl2 in ranglist:
            su1 = 0
            su2 = 0
            for p1, s1 in ranglist[pl1].items():
                for p2, s2 in ranglist[pl2].items():
                    if p1 == p2:
                        su1 += s1
                        su2 += s2
            if su1 > su2:
                ranglist.pop(pl2)
            elif su2 > su1:
                ranglist.pop(pl1)
    line = input()
result = {}
for pl, sk in ranglist.items():
    sumata = 0
    for ski in sk:
        sumata += sk[ski]
    result[pl] = sumata
result = dict(reversed(sorted(result.items(), key=lambda x: x[1])))
for p in result:
    print(f'{p}: {result[p]} skill')
    new = dict(reversed(sorted(ranglist[p].items())))
    new = dict(reversed(sorted(new.items(), key=lambda x: x[1])))
    for s in new:
        print(f'- {s} <::> {new[s]}')
