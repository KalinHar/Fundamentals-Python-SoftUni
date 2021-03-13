numbers = [int(x) for x in input().split(' ')]
top_5 = []
average = sum(numbers) / len(numbers)
numbers = reversed(sorted(numbers))
for num in numbers:
    if num > average:
        top_5.append(num)
        if len(top_5) == 5:
            break
    else:
        break
if top_5:
    print(' '.join([str(x) for x in top_5]))
else:
    print('No')
