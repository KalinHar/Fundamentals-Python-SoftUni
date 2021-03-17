import re
n = int(input())
lines = []
for _ in range(n):
    lines.append(input())
regex1 = r"@\w+\|"
regex2 = r"#\d+\*"
for text in lines:
    name = re.findall(regex1, text)
    age = re.findall(regex2, text)
    print(f"{name[0][1:-1]} is {age[0][1:-1]} years old.")
