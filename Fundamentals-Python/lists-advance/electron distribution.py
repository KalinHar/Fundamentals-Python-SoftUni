n = int(input())
res = []
for i in range(1, n + 1):
    k = 2 * (i ** 2)
    diff = n - k
    if diff <= 0:
        res.append(n)
        break
    else:
        res.append(k)
        n = diff
print(res)
