n = int(input())
highest = 0
for i in range(n):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if highest < snowball_value:
        highest = snowball_value
        snow = snowball_snow
        time = snowball_time
        quality = snowball_quality
print(f'{snow} : {time} = {highest} ({quality})')
