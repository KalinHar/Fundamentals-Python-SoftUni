text = input().split('|')
budget = float(input())
f_budget = budget
new_price = []
for element in text:
    article, price= element.split('->')
    price = float(price)
    if (article == 'Clothes' and price <= 50) \
            or (article == 'Shoes' and price <= 35) \
            or (article == 'Accessories' and price <= 20.50):
        if budget >= price:
            budget -= price
            new_price.append(price * 1.4)
    if budget == 0:
        break
if len(new_price) >= 1:
    total = sum(new_price) + budget
    for pr in new_price:
        print(f"{pr:.2f}", end=' ')
    print("")
    print(f'Profit: {total - f_budget:.2f}')
    if total >= 150:
        print('Hello, France!')
    else:
        print('Time to go.')
