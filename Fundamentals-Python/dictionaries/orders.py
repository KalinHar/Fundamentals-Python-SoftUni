line = input()
products = {}
while line != "buy":
    line = line.split(' ')
    if line[0] not in products:
        products[line[0]] = [float(line[1]), int(line[2])]
    else:
        products[line[0]][0] = float(line[1])
        products[line[0]][1] += int(line[2])
    line = input()
for p in products:
    print(f"{p} -> {products[p][0] * products[p][1]:.2f}")
