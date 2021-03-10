text = input()
symbols = {}
for i in text:
    if i != ' ':
        if i not in symbols:
            symbols[i] = 0
        symbols[i] += 1
for s in symbols:
    print(f"{s} -> {symbols[s]}")
