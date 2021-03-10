n = int(input())
register = {}
for i in range(n):
    line = input().split(' ')
    if line[0] == 'register':
        if line[1] not in register:
            register[line[1]] = line[2]
            print(f'{line[1]} registered {line[2]} successfully')
        else:
            print(f'ERROR: already registered with plate number {register[line[1]]}')
            continue
    else:
        if line[1] not in register:
            print(f'ERROR: user {line[1]} not found')
            continue
        else:
            print(f'{line[1]} unregistered successfully')
            register.pop(line[1])
for r in register:
    print(f'{r} => {register[r]}')
