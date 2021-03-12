text = input().split(', ')
action = input()
while action != 'Craft!':
    action = action.split(' - ')
    if 'Collect' in action and action[1] not in text:
        text.append(action[1])
    elif 'Drop' in action and action[1] in text:
        text.remove(action[1])
    elif 'Combine Items' in action:
        combi = action[1].split(':')
        if combi[0] in text:
            new_text = []
            for t in text:
                new_text.append(t)
                if t == combi[0]:
                    new_text.append(combi[1])
            text = new_text
    elif 'Renew' in action:
        if action[1] in text:
            new_text = []
            for t in text:
                if action[1] != t:
                    new_text.append(t)
            new_text.append(action[1])
            text = new_text
    action = input()
print(', '.join(text))
