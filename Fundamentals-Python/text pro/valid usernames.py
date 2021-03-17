users = [x for x in input().split(', ') if 3 <= len(x) <= 16]
valid_users = []

for user in users:
    valid_char = True
    for char in user:
        if char.isalnum() or char == '-' or char == '_':
            continue
        else:
            valid_char = False
            break
    if valid_char:
        valid_users.append(user)

for v in valid_users:
    print(v)
