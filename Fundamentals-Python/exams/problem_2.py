import re

n = int(input())
pattern = r"!(?P<command>[A-Z][a-z]{2,})!:\[(?P<text>[A-Za-z]{8,})\]"

for _ in range(n):
    line = input()
    matches = re.findall(pattern, line)
    if not matches:
        print("The message is invalid")
    else:
        for match in re.finditer(pattern, line):
            encrypt = [str(ord(x)) for x in match.group("text")]
            print(f"{match.group('command')}: {' '.join(encrypt)}")

