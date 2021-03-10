line_c = input()
contests = {}
while line_c != 'end of contests':
    line_c = line_c.split(':')
    contests[line_c[0]] = line_c[1]
    line_c = input()
line_s = input()
students = {}
while line_s != 'end of submissions':
    line_s = line_s.split('=>')
    subject = line_s[0]
    name = line_s[2]
    if subject in contests and contests[subject] == line_s[1]:
        if name not in students:
            exam = {}
            exam[subject] = int(line_s[3])
            students[name] = exam
        else:
            if subject not in students[name]:
                students[name].update({subject:int(line_s[3])})
            else:
                if int(line_s[3]) > students[name][subject]:
                    students[name][subject] = int(line_s[3])
    line_s = input()
max_p = 0
for n, s in students.items():
    points = 0
    for p in s.values():
        points += p
    if points > max_p:
        max_p = points
        max_st = n
print(f'Best candidate is {max_st} with total {max_p} points.')
print('Ranking:')
students = dict(sorted(students.items()))
for n, s in students.items():
    print(n)
    s = dict(reversed(sorted(s.items(), key=lambda x: x[1])))
    for c, r in s.items():
        print(f'#  {c} -> {r}')
