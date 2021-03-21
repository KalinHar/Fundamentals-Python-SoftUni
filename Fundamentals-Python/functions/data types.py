def types(entry,num):
    res = None
    if entry == 'int':
        num = int(num)
        res = 2 * num
    elif entry == 'real':
        num = float(num)
        res = (f'{1.5 * num:.2f}')
    else:
        res = "$" + num + '$'
    return res


line = input()
dig = input()
print(types(line, dig))
