n = int(input())
dictionary = {}
for i in range(n):
    word = input()
    sino = input()
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(sino)
for (key, values) in dictionary.items():
    print(f"{key} - {', '.join(values)}")
