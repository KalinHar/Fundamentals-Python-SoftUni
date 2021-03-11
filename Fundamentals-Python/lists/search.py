n = int(input())
word = input()
strings = []
result = []
for i in range(n):
    text = input()
    strings.append(text)
    if word in text:
        result.append(text)
print(strings)
# for s in strings:
#     if word not in s:
#         strings.remove(s)
# print(strings)
print(result)
