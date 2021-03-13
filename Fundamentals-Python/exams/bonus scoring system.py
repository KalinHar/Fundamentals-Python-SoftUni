from math import ceil
count_students = int(input())
count_lectures = int(input())
bonus = int(input())
max_bonus = 0
max_lecture = 0
for st in range(count_students):
    st_attend = int(input())
    total = st_attend / count_lectures * (5 + bonus)
    if max_bonus < total:
        max_bonus = total
        max_lecture = st_attend
print(f'Max Bonus: {ceil(max_bonus)}.')
print(f'The student has attended {max_lecture} lectures.')
