lost = int(input())
helmet_pr = float(input())
sword_pr = float(input())
shield_pr = float(input())
armor_pr = float(input())
cost = 0
count = 0
for i in range(1, lost + 1):
    if i % 2 == 0:
        cost += helmet_pr
    if i % 3 == 0:
        cost += sword_pr
    if i % 2 == 0 and i % 3 == 0:
        count += 1
        cost += shield_pr
        if count % 2 == 0:
            cost += armor_pr
print(f'Gladiotor expenses: {cost:.2f} aureus')