import math
first_empl = int(input())
second_empl = int(input())
third_empl = int(input())
people = int(input())
empl = first_empl + second_empl + third_empl
time = people / empl
if time > 3:
    rest = time // 3
    if time % 3 == 0:
        rest -= 1
    time += rest
    time = math.ceil(time)
else:
    time = math.ceil(time)
print(f'Time needed: {time}h.')