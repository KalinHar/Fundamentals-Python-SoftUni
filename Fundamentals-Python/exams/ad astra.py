import re

pattern = r"(\||#)(?P<food>[A-z a-z0-9]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<cal>\d{1,5})\1"

total_cal = 0
line = input()

for match in re.finditer(pattern,line):
    if int(match.group("cal")) <= 10000:
        total_cal += int(match.group("cal"))

print(f"You have food to last you for: {total_cal // 2000} days!")

for match in re.finditer(pattern,line):
    print(f"Item: {match.group('food')}, Best before: {match.group('date')}, Nutrition: {match.group('cal')}")
