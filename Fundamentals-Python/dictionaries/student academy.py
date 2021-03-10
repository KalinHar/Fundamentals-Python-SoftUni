n = int(input())
students = {}
for _ in range(n):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

excellent = {}
for s in students:
    average_grade = sum(students[s]) / len(students[s])
    if average_grade >= 4.50:
        excellent[s] = average_grade

for e, g in sorted(excellent.items(), key=lambda x: -x[1]):
    print(f'{e} -> {g:.2f}')
