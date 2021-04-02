import re
text = input()
regex = r"(^|\s)[a-z]+[-_\.]?[a-z]+@[a-z-]+\.[a-z-]+\.?[a-z]+?\b"
result = re.finditer(regex, text)
for r in result:
    print(r.group())
