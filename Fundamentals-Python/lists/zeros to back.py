text = input()
text = text.split(', ')
normal = []
zeroes = []
for element in text:
    element = int(element)
    if element == 0:
        zeroes.append(element)
    else:
        normal.append(element)
print(normal + zeroes)
