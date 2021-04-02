import re
text = ""
while True:
    line = input()
    if line:
        text += line + " "
    else:
        break

pattern = r"\d+"
result = re.findall(pattern, text)
print(" ".join(result))
