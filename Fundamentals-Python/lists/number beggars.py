sting = input()
beggar = int(input())
numbers = sting.split(', ')
result = []
suma = 0
for b in range(beggar):
    for n in range(b, len(numbers), beggar):
        suma += int(numbers[n])
    result.append(suma)
    suma = 0
print(result)
