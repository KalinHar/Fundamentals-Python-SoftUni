import re
text = input()
regex = r"\b(?P<day>\d{2})(?P<sep>[\.-\\/)(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"
# result = re.findall(regex, text)
# for r in result:
#     print(f" D - {r[0]}, Y - {r[3]}, M - {r[2]}, s'{r[1]}'")
# print(result)
dict_matches = [obj.groupdict() for obj in re.finditer(regex, text)]
matches = re.finditer(regex, text)
for match in matches:
    print(f"Day: {match.group('day')}, Month: {match.group('month')}, Year: {match.group('year')}")

