rows = int(input())
free = []
kate_steps = []
count = 0
kate_out = False

for r in range(rows):
    line = input()
    for l in range(len(line)):
        if line[l] == ' ':
            space = [r, l]
            free.append(space)
        elif line[l] == 'k':
            kate = [r, l]
            kate_steps.append(kate)

if kate[0] == 0 or kate[0] == (rows - 1) or \
        kate[1] == (len(line) - 1) or kate[1] == 0:
    kate_out = True

if not kate_out:
    for k in kate_steps:
        k_moves = [[k[0]-1, k[1]], [k[0]+1, k[1]], [k[0], k[1]-1], [k[0], k[1]+1]]
        for move in k_moves:
            if move in free:
                kate_steps.append(move)
                free.remove(move)
                if move[0] == 0 or move[0] == (rows - 1) or \
                        move[1] == (len(line) - 1) or move[1] == 0:
                    kate_out = True
                    break
        count += 1
        if kate_out:
            break

if kate_out:
    print(f'Kate got out in {count + 1} moves')
else:
    print('Kate cannot get out')
