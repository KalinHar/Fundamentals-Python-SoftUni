mine = {}
line = input()
while line != 'stop':
    quanty = int(input())
    if line not in mine:
        mine[line] = 0
    mine[line] += quanty
    line = input()
for m in mine:
    print(f"{m} -> {mine[m]}")
