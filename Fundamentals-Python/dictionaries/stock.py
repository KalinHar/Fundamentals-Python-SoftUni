line = input().split(' ')
stocks = {}
search_pr = input().split(' ')
for i in range(0, len(line), 2):
    key = line[i]
    value = line[i + 1]
    stocks[key] = int(value)
for searched in search_pr:
    if searched in stocks:
        print(f'We have {stocks[searched]} of {searched} left')
    else:
        print(f"Sorry, we don't have {searched}")

elements = input().split(" ")
bakery = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    bakery[key] = int(value)
print(bakery)
