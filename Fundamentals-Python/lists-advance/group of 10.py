from math import ceil
numbers = [int(x) for x in input().split(', ')]
n = ceil(max(numbers) / 10)
for i in range(1, n + 1):
    res = []
    for num in numbers:
        if num <= i * 10:
            res.append(num)
    numbers = [x for x in numbers if x not in res]
    print(f"Group of {i * 10}'s: {res}")
