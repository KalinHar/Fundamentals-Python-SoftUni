symb1 = ord(input())
symb2 = ord(input())
text = input()
result = 0
for s in text:
    if symb1 < ord(s) < symb2:
        result += ord(s)
print(result)
