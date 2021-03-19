import re

pattern = r"(=|/)(?P<dest>[A-Z][a-zA-Z]{2,})\1"

line = input()
destin = []

travel_points = 0
for d in re.finditer(pattern, line):
    destin.append(d.group("dest"))
    travel_points += len(d.group("dest"))
print(f"Destinations: {', '.join(destin)}")
print(f"Travel Points: {travel_points}")
