def tribon(n):
    numbers = [0, 0, 1]
    for i in range(1, n):
        last = sum(numbers[-3:])
        numbers.append(last)
    numbers = numbers[2:]
    numbers = [str(x) for x in numbers]
    res = ' '.join(numbers)
    return res


num = int(input())
print(tribon(num))