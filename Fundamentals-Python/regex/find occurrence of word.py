import re
text = input().lower()
word = input().lower()
word = "\\b" + word + "\\b"  # rf"\b{word}\b
pattern = word
result = re.findall(pattern, text)
# print(",".join(result))
print(len(result))
