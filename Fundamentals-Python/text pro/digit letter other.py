text = input()
digits = ""
alfa = ""
other = ""
for s in text:
    if s.isdigit():
        digits += s
    elif s.isalpha():
        alfa += s
    else:
        other += s
print(digits)
print(alfa)
print(other)
