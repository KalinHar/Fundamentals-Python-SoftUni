import re

text = input()
reg_title = r"(?<=<title>).+(?=</title>)"
reg_text = r'<[A-Za-z ="\.:/]+>|\\n'

result = re.findall(reg_text, text)
title = re.findall(reg_title, text)

while result:
    text = text.replace(result[0], "", 1)
    result.pop(0)

text = text.replace(title[0],"",1)
output = text.split()
print(f"Title: {title[0]}")
print("Content:",end=' ')
print(*output,sep=" ")
