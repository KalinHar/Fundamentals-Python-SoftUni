text = input().split(' ')
numbers = [int(x) for x in text]


def exchange(array, index):
    if index < 0:
        index += len(array)
    first = array[: index + 1]
    second = array[index + 1 :]
    array = second + first
    return array


def max_min(maxmin, oddevan, array):
    if oddevan == 'odd':
        result = [x for x in array if x % 2 != 0]
    else:
        result = [x for x in array if x % 2 == 0]
    if not result:
        print('No matches')
    else:
        if maxmin == 'max':
            el_max = max(result)
            for m in range(len(array) - 1, -1, -1):
                if array[m] == el_max:
                    print(m)
                    break
        else:
            el_min = min(result)
            for m in range(len(array) - 1, -1, -1):
                if array[m] == el_min:
                    print(m)
                    break


def first_last(firstlast, count, oddevan, array):
    new_result = []
    if oddevan == 'odd':
        result = [x for x in array if x % 2 != 0]
    else:
        result = [x for x in array if x % 2 == 0]
    if firstlast == 'first':
        for el in result:
            new_result.append(el)
            if count == len(new_result):
                break
    else:
        for el in reversed(result):
            new_result.insert(0, el)
            if count == len(new_result):
                break
    print(new_result)


command = input()
while command != 'end':
    command = command.split(' ')
    if command[0] == 'exchange':
        if - len(numbers) <= int(command[1]) <= len(numbers) - 1:
            numbers = exchange(numbers, int(command[1]))
        else:
            print('Invalid index')
    elif command[0] in 'maxmin':
        max_min(command[0], command[1], numbers)
    elif command[0] in 'firstlast':
        if int(command[1]) > len(numbers):
            print('Invalid count')
        else:
            first_last(command[0], int(command[1]), command[2], numbers)
    command = input()
print(numbers)
