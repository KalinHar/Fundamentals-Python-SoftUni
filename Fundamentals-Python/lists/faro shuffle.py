sting = input()
n = int(input())
cards = sting.split(' ')
result = []
count = int(len(cards) / 2)
for s in range(n):
    for i in range(count):
        result.append(cards[i])
        result.append(cards[count + i])
    cards = result
    result = []
print(cards)
