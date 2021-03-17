word = input()
result = {}
while word != 'end':
    result[word] = word[:: -1]
    word = input()
for w, rw in result.items():
    print(f"{w} = {rw}")
