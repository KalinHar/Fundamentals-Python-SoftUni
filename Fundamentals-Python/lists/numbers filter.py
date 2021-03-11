n = int(input())
numbers = []
result = []
for i in range(n):
    numbers.append(int(input()))
comm = input()
if comm == 'even':
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
elif comm == 'odd':
    for num in numbers:
        if num % 2 != 0:
            result.append(num)
elif comm == 'positive':
    for num in numbers:
        if num >= 0:
            result.append(num)
elif comm == 'negative':
    for num in numbers:
        if num < 0:
            result.append(num)
print(result)
