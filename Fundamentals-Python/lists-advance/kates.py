rows = int(input())
free = []
for r in range(rows):
    line = input()
    for l in range(len(line)):
        if line[l] == ' ':
            space = [r, l]
            free.append(space)
        elif line[l] == 'k':
            kate = [r, l]
total = 0
flag = total
while free:
    flag = total
    for f in free:
        if (kate[0] - 1 == f[0] and kate[1] == f[1]) or \
                (kate[0] + 1 == f[0] and kate[1] == f[1]) or \
                (kate[0] == f[0] and kate[1] - 1 == f[1]) or \
                (kate[0] == f[0] and kate[1] + 1 == f[1]):
            kate = f
            free.remove(f)
            total += 1
        if kate[0] == 0 or kate[0] == (rows - 1) or \
                kate[1] == (len(line) - 1) or kate[1] == 0:
            free = []
            break
    if flag == total:
        break
if kate[0] == 0 or kate[0] == (rows - 1) or \
                kate[1] == (len(line) - 1) or kate[1] == 0:
    total += 1
    print(f'Kate got out in {total} moves')
if flag == total:
    print('Kate cannot get out')

