rows = int(input())
free = []
kate_way = []
kate_out = False
for r in range(rows):
    line = input()
    for c in range(len(line)):
        if line[c] == ' ':
            space = [r, c]
            free.append(space)
        elif line[c] == 'k':
            kate = [r, c]
            kate_way.append(kate)
            if r == 0 or r == (rows - 1) or \
                    c == (len(line) - 1) or c == 0:
                kate_out = True
count = 0
while not kate_out:
    flag = count
    for k in kate_way:
        for f in free:
            if (k[0] - 1 == f[0] and k[1] == f[1]) or \
                    (k[0] + 1 == f[0] and k[1] == f[1]) or \
                    (k[0] == f[0] and k[1] - 1 == f[1]) or \
                    (k[0] == f[0] and k[1] + 1 == f[1]):
                kate_way.append(f)
                free.remove(f)
                count += 1
                if f[0] == 0 or f[0] == (rows - 1) or \
                        f[1] == (len(line) - 1) or f[1] == 0:
                    kate_out = True
                    break
        if kate_out:
            break
    if flag == count or kate_out:
        break

if kate_out:
    print(f'Kate got out in {count + 1} moves')
else:
    print('Kate cannot get out')

