rows = int(input())
matrix = []
# for r in range(rows):
#     el = []
#     line = input()
#     for l in range(len(line)):
#         el.append(line[l])
#         if line[l] == 'k':
#             kate = [r, l]
#     matrix.append(el)

matrix = [[l for l in input()] for r in range(rows)]
columns = len(matrix[0])
for i in range(rows):
    for j in range(columns):
        if matrix[i][j] == 'k':
            kate = [i, j]
        print(matrix[i][j], end = "")
    print()
print(kate)

a = f"""Lorem ipsum dolor sit 
amet,consectetur adipiscing
elit, sed do eiusmod tempor 
incididuntut labore et
dolore magna {kate} aliqua."""

print(a)