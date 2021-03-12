def decri(text):
    char = ''
    strings = ''
    for t in text:
        if '0' <= t <= '9' and len(char) < 3:
            char += t
        else:
            strings += t
    char = chr(int(char))
    if len(strings) > 1:
        strings = strings[-1:] + strings[1:-1] + strings[:1]
    res = char + strings
    return res


message = input().split(' ')
new_mess = []
for m in message:
    new_mess.append(decri(m))
print(' '.join(new_mess))
