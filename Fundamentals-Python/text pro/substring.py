flag = input()
text = input()
while flag in text:
    text = text.replace(flag, "")
print(text)
