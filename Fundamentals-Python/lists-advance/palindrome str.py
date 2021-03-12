strings = input().split(' ')
searched = input()
palin = []
for s in strings:
    if s == ''.join(reversed(s)):
        palin.append(s)
print(palin)
print(f'Found palindrome {palin.count(searched)} times')
