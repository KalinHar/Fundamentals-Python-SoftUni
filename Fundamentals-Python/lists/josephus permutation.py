text = input()
text = text.split(' ')
num = int(input())
k = num - 1
killed = []
while text:
    if k >= len(text):
        k -= len(text)
    else:
        killed.append(text.pop(k))
        k += (num - 1)
result = ','.join(killed)
print(f'[{result}]')
