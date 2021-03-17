path = input()
name = None
extension = None
for index in range(len(path)-1, -1, -1):
    if ord(path[index]) == 92:
        name, extension = path[index+1:].split('.')
        break
print(f'File name: {name}')
print(f'File extension: {extension}')
