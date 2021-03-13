empl1 = int(input())
empl2 = int(input())
empl3 = int(input())
students_count = int(input())
students_per_hour = empl3 + empl2 + empl1
result = students_count // students_per_hour
rest_students = students_count % students_per_hour
if rest_students > 0:
    result += 1
one_hour_brake = result // 3
if result % 3 == 0:
    one_hour_brake -= 1
result += one_hour_brake
if result == -1:
    result = 0
print(f'Time needed: {result}h.')
