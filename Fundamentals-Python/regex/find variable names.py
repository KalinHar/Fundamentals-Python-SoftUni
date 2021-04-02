import re
text = input()

pattern = r"(?<=\b_)[0-9a-zA-Z]+(?=\b)"
result = re.findall(pattern, text)
print(",".join(result))
