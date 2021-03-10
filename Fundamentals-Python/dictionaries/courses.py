line = input()
courses = {}
while line != 'end':
    line = line.split(' : ')
    if line[0] not in courses:
        courses[line[0]] = []
    courses[line[0]].append(line[1])
    line = input()
courses = dict(sorted(courses.items(), key=lambda x: x[0].upper()))
courses = dict(sorted(courses.items(), key=lambda x: len(x[1])))
courses = dict(reversed(courses.items()))
for (cour, stud) in courses.items():
    print(f'{cour}: {len(stud)}')
    stud.sort()
    for st in stud:
        print(f'-- {st}')
