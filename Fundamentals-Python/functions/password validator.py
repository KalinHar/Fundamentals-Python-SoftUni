def validator(password):
    valid = True
    digits = '0123456789'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    if not 6 <= len(password) <= 10:
        print('Password must be between 6 and 10 characters')
        valid = False
    for p in password:  # if password.isalnum  => (a-z, 0-9)
        if p in digits:
            count += 1
        if not (p in digits or p.lower() in alphabet):  # if not (p.isdigit or p.isalpha)
            print('Password must consist only of letters and digits')
            valid = False
            break
    if count < 2:
        print('Password must have at least 2 digits')
        valid = False
    if valid:
        print('Password is valid')


text = input()
validator(text)