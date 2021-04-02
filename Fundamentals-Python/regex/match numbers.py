import re
text = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
result = re.finditer(pattern, text)
for r in result:
    print(r.group(), end=" ")
