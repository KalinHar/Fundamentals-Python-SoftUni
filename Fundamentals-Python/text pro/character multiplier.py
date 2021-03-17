first, second = sorted(input().split(' '), key=lambda x: len(x))
total_sum = 0
diff = len(first) - len(second)

for i in range(len(first)):
    total_sum += ord(first[i]) * ord(second[i])
if diff < 0:
    for i in range(diff, 0):
        total_sum += ord(second[i])

print(total_sum)
