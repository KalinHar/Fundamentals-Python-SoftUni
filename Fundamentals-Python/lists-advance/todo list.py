note = []
command = input()
while command != 'End':
    note.append(command.split('-'))
    command = input()
for n in range(len(note)):
    note[n][0] = int(note[n][0])
note.sort()
result = [el[1] for el in note]
print(result)

# place = []
# note = []
# result = []
# command = input()
# while command != 'End':
#     command = command.split('-')
#     place.append(int(command[0]))
#     note.append(command[1])
#     command = input()
# while place:
#     a = place.index(min(place))  # indeksa na min element v lista
#     result.append(note[a])
#     place.pop(a)
#     note.pop(a)
# print(result)
