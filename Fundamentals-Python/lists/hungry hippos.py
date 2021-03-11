rows = int(input())
hippos = []
for r in range(rows):
    line = input().split(' ')
    for l in range(len(line)):
        if line[l] == '1':
            hip = [r, l]
            hippos.append(hip)
res = []
total = []
while hippos:
    res.append(hippos[0])
    hippos.pop(0)
    for f in res:
        for h in hippos:
            if ((h[0] == f[0] and h[1] - 1 == f[1]) or (h[0] - 1 == f[0] and h[1] == f[1])) and h not in res:
                res.append(h)
            if f[0] >= 1 and f[1] >= 1:
                if ((h[0] == f[0] and h[1] + 1 == f[1]) or (h[0] + 1 == f[0] and h[1] == f[1])) and h not in res:
                    res.append(h)
    total.append(res)
    hippos = [h for h in hippos if h not in res]
    res = []
print(len(total))
