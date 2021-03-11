n = int(input())
poss = []
negg = []

for i in range(n):
    num = int(input())
    if num >= 0:
        poss.append(num)
    else:
        negg.append(num)
print(poss)
print(negg)
print(f'Count of positives: {len(poss)}. Sum of negatives: {sum(negg)}')
