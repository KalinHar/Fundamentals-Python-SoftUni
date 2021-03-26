n = int(input())
liters = 0
for i in range(n):
    quant = int(input())
    liters += quant
    if liters > 255:
        liters -= quant
        print('Insufficient capacity!')
print(liters)
