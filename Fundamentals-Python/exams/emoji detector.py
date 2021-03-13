text =input()
cool = [int(n) for n in text if '0' <= n <= '9']
sum_cool = 1
for c in cool:
    sum_cool *= c
print(f'Cool threshold: {sum_cool}')
emoji = ''
total = []
for t in text:
    if t == ':':
        if emoji == ':' or (len(emoji) >= 5 and emoji[0] == ':' and emoji[-2] != ':'):
            emoji += t
        elif emoji == '::':
            emoji = '::'
        else:
            emoji = ':'
    elif t == '*':
        if emoji == '*' or (len(emoji) >= 5 and emoji[0] == '*' and emoji[-2] != '*'):
            emoji += t
        elif emoji == '**':
            emoji = '**'
        else:
            emoji = '*'
    elif len(emoji) >= 2:
        if len(emoji) == 2 and 'A' <= t <= 'Z':
            emoji += t
        elif len(emoji) > 2 and 'a' <= t <= 'z' and emoji[-1] != ':' and emoji[-1] != '*':
            emoji += t
        else:
            emoji = ''
    else:
        emoji = ''
    if len(emoji) >= 5 and (emoji[-2] + emoji[-1] == '::' or emoji[-2] + emoji[-1] == '**'):
        total.append(emoji)
        emoji = ''
fun = []
for t in total:
    sum = 0
    for i in t:
        if i != ':' and i != '*':
            sum += ord(i)
    if sum >= sum_cool:
        fun.append(t)
print(f'{len(total)} emojis found in the text. The cool ones are:')
if fun:
    for f in fun:
        print(f)

