line = input()
contests = {}
individual = {}
while line != 'no more time':
    line = line.split(' -> ')
    user = line[0]
    contest = line[1]
    points = int(line[2])
    student = {user: points}
    if contest not in contests:
        contests[contest] = student
    else:
        if user not in contests.items():
            contests[contest].update(student)
        else:
            if contests[contest][user] < points:
                contests[contest][user] = points
    line = input()
for c in contests:
    print(f'{c}: {len(contests[c])} participants')
    count = 1
    contests[c] = dict(reversed(sorted(contests[c].items())))
    contests[c] = dict(reversed(sorted(contests[c].items(), key=lambda x: x[1])))
    for st, po in contests[c].items():
        print(f'{count}. {st} <::> {po}')
        count += 1
        if st not in individual:
            individual[st] = po
        else:
            individual[st] += po
print('Individual standings:')
count = 1
individual = dict(reversed(sorted(individual.items())))
individual = dict(reversed(sorted(individual.items(), key=lambda x: x[1])))
for s, p in individual.items():
    print(f'{count}. {s} -> {p}')
    count += 1
