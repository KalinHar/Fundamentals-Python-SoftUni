import re
pattern = r"www\.[A-Za-z0-9-]+(\.[a-z]+)+"
text = ""
while True:
    line = input()
    if line:
        text += line + " "
    else:
        break

result = re.finditer(pattern, text)
for r in result:
    print(r.group())
