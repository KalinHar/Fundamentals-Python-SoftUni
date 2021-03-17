text = input()
for em in range(len(text)):
    if text[em] == ':':
        print(text[em:em+2])
