key = int(input())
n = int(input())
mess = ''
for l in range(n):
    letter = input()
    mess += chr(ord(letter) + key)
print(mess)
