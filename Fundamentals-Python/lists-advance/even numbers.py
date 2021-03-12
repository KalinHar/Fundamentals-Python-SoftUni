numbers = list(map(int, input().split(', ')))
result = [n for n in range(len(numbers)) if numbers[n] % 2 == 0]
print(result)
