employees = [int(x) for x in input().split(' ')]
factor = int(input())
employees = [x*3 for x in employees]
average = sum(employees) / len(employees)
count = 0
for man in employees:
    if man >= average:
        count += 1
print(f'Score: {count}/{len(employees)}. ', end='')
if count >= len(employees) / 2:
    print('Employees are happy!')
else:
    print('Employees are not happy!')
