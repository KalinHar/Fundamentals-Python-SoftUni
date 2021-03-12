numbers = input().split(' ')
message = input()
for i in range(len(numbers)):
    suma = 0
    for n in numbers[i]:
        suma += int(n)
    numbers[i] = suma
res = ''
for i in range(len(numbers)):
    if numbers[i] > len(message):
        posit = numbers[i] % len(message)
    else:
        posit = numbers[i]
    res += message[posit]
    message = message.replace(message[posit], '', 1)
print(res)
