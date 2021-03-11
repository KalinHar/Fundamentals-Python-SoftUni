text = input()
numbers = text.split(' ')
for index in range(len(numbers)):
    numbers[index] = int(numbers[index])
num = int(input())
for i in range(num):
    numbers.remove(min(numbers))
print(numbers)
