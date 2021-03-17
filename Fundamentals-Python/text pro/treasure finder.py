import re
keys = [int(x) for x in input().split()]
line = input()
while line != 'find':
    result = ''
    for i in range(len(line)):
        if i >= len(keys):
            i_k = i % len(keys)
        else:
            i_k = i
        result += chr(ord(line[i]) - keys[i_k])
    reg1 = r"&\w+&"
    reg2 = r"<\w+>"
    treasure = re.findall(reg1, result)
    courds = re.findall(reg2, result)
    print(f'Found {treasure[0][1:-1]} at {courds[0][1:-1]}')
    line = input()
