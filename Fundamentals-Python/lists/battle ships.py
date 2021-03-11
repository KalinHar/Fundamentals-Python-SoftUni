count = 0
rows = int(input())
ships = []
for r in range(rows):
    row = input().split(' ')
    for n in range(len(row)):
        row[n] = int(row[n])
    ships.append(row)
attack = input().split(' ')
for a in attack:
    sh = int(ships[int(a[0])][int(a[2])])
    if sh > 0:
        sh -= 1
        if sh == 0:
            count += 1
        ships[int(a[0])][int(a[2])] = sh
print(count)
