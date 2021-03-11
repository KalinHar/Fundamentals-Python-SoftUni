row_1 = input()
row_1 = row_1.split(' ')
for i in range(len(row_1)):
    row_1[i] = int(row_1[i])
row_2 = input()
row_2 = row_2.split(' ')
for i in range(len(row_2)):
    row_2[i] = int(row_2[i])
row_3 = input()
row_3 = row_3.split(' ')
for i in range(len(row_3)):
    row_3[i] = int(row_3[i])
first = False
second = False
if (row_1[0] == 1 and row_1[1] == 1 and row_1[2] == 1) or \
    (row_2[0] == 1 and row_2[1] == 1 and row_2[2] == 1) or \
    (row_3[0] == 1 and row_3[1] == 1 and row_3[2] == 1):
    first = True
if (row_1[0] == 1 and row_2[0] == 1 and row_3[0] == 1) or \
    (row_1[1] == 1 and row_2[1] == 1 and row_3[1] == 1) or \
    (row_1[2] == 1 and row_2[2] == 1 and row_3[2] == 1):
    first = True
if (row_1[0] == 1 and row_2[1] == 1 and row_3[2] == 1) or \
    (row_1[2] == 1 and row_2[1] == 1 and row_3[0] == 1):
    first = True
if sum(row_1) == 6 or sum(row_2) == 6 or sum(row_3) == 6:
    second = True
if (row_1[0] == 2 and row_2[0] == 2 and row_3[0] == 2) or \
    (row_1[1] == 2 and row_2[1] == 2 and row_3[1] == 2) or \
    (row_1[2] == 2 and row_2[2] == 2 and row_3[2] == 2):
    second = True
if (row_1[0] == 2 and row_2[1] == 2 and row_3[2] == 2) or \
    (row_1[2] == 2 and row_2[1] == 2 and row_3[0] == 2):
    second = True
if first:
    print('First player won')
elif second:
    print('Second player won')
else:
    print('Draw!')
