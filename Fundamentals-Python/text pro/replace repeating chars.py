text = input()
same = None
for ch in text:
    if ch != same:
        print(ch, end='')
        same = ch
