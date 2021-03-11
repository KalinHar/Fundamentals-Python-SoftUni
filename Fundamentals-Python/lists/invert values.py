string = input()
numbers = string.split(' ')
for num in range(len(numbers)):
    numbers[num] = -1 * int(numbers[num])
print(numbers)
