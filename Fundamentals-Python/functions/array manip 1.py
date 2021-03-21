def odd_or_evan(oddevan, array):
    if oddevan == 'odd':
        result = [x for x in array if x % 2 != 0]
    else:
        result = [x for x in array if x % 2 == 0]
    return result


def exchange(array, index):
    if 0 <= int(index) <= len(array) - 1:  # -2 # if index < 0: # index += len(array)
        first = array[:index + 1]
        second = array[index + 1:]
        array = second + first
    else:
        print('Invalid index')
    return array


def max_min(maxmin, oddevan, array):
    result = odd_or_evan(oddevan, array)
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
    if int(count) > len(array):
        print('Invalid count')
    else:
        new_result = []
        result = odd_or_evan(oddevan, array)
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


text = input().split(' ')
numbers = [int(x) for x in text]
command = input()
while command != 'end':
    command = command.split(' ')
    if command[0] == 'exchange':
        numbers = exchange(numbers, int(command[1]))
    elif command[0] in 'maxmin':
        max_min(command[0], command[1], numbers)
    elif command[0] in 'firstlast':
        first_last(command[0], int(command[1]), command[2], numbers)
    command = input()
print(numbers)
