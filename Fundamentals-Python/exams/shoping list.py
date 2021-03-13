text = input()
text = text.split('!')
command = input()
while command != 'Go Shopping!':
    if ' ' in command:
        command = command.split(' ')
        new_text = []
        if command[0] == 'Urgent' and command[1] not in text:
            new_text.append(command[1])
            text = new_text + text
        elif command[0] == 'Unnecessary' and command[1] in text:
            text.remove(command[1])
        elif command[0] == 'Correct' and command[1] in text and len(command) == 3:
            for t in text:
                if command[1] == t:
                    new_text.append(command[2])
                else:
                    new_text.append(t)
            text = new_text
        elif command[0] == 'Rearrange' and command[1] in text:
            for t in text:
                if command[1] == t:
                    last = t
                else:
                    new_text.append(t)
            new_text.append(last)
            text = new_text
    command = input()
print(', '.join(text))
