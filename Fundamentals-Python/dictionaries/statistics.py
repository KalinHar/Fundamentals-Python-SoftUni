line = input()
stocks = {}
while line != 'statistics':
    product, value = line.split(': ')
    if product not in stocks:
        stocks[product] = int(value)
    else:
        stocks[product] += int(value)
    line = input()
print('Products in stock:')
for pr in stocks:
    print(f'- {pr}: {stocks[pr]}')
print(f'Total Products: {len(stocks)}')
print(f'Total Quantity: {sum(stocks.values())}')
