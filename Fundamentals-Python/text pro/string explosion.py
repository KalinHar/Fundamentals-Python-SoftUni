line = input()
rest = ''

while line:
    count = 0
    for index in range(len(line)):
        if index == len(line)-1:
            rest += line
            line = ''
            break
        if line[index] == '>':
            rest += line[:index+1]
            count = int(line[index+1])
            line = line[index+1:]
            break
    while count:
        if len(line) == 1:
            if line == '>':
                rest += '>'
                line = ''
                count = 0
            else:
                line = ''
                count = 0
        elif line[0] != '>':
            line = line[1:]
            count -= 1
        else:
            line = line[1:]
            rest += '>'
            count += int(line[0])

print(rest)