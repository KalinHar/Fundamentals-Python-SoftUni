key = input()
command = input()
new_key = ''
while command != 'Generate':
    command = command.split('>>>')
    if "Contains" in command:
        if command[1] in key:
            print(f'{key} contains {command[1]}')
        else:
            print('Substring not found!')
    elif "Flip" in command:
        if command[1] == 'Upper':
            for s in range(len(key)):
                if s in range(int(command[2]), int(command[3])):
                    new_key += key[s].upper()
                else:
                    new_key += key[s]
            print(new_key)
            key = new_key
        if command[1] == 'Lower':
            for s in range(len(key)):
                if s in range(int(command[2]), int(command[3])):
                    new_key += key[s].lower()
                else:
                    new_key += key[s]
            print(new_key)
            key = new_key
    elif "Slice" in command:
        for s in range(len(key)):
            if s not in range(int(command[1]), int(command[2])):
                new_key += key[s]
        print(new_key)
        key = new_key
    new_key = ''
    command = input()
print(f'Your activation key is: {key}')
