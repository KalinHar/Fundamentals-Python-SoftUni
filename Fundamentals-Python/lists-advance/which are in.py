word = input().split(', ')
text = input().split(', ')
# result = []
# for w in word:
#     for t in text:
#         if w in t and w not in result:
#             result.append(w)
# print(result)

result = [w for w in word for t in text if w in t]
print(sorted(set(result), key= result.index))
