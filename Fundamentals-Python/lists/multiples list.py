factor = int(input())
count = int(input())
result = [factor]
multi = factor
for i in range(count - 1):
    multi += factor
    result.append(multi)
print(result)
