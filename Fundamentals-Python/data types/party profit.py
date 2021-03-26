companions = int(input())
days = int(input())
profit = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        companions -= 2
    if i % 15 == 0:
        companions += 5
    profit += 50
    profit -= (2 * companions)
    if i % 3 == 0:
        profit -= (3 * companions)
    if i % 5 == 0:
        profit += (20 * companions)
    if i % 3 == 0 and i % 5 == 0:
        profit -= (2 * companions)
print(f'{companions} companions received {int(profit / companions)} coins each.')

