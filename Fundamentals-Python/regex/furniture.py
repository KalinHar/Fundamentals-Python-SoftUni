import re

pattern = r"^>>(?P<name>\w+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)$"
line = input()
furnit = []
total = 0

while line != "Purchase":
    match = re.match(pattern, line)
    if match:
        data = match.groupdict()
        furnit.append(data["name"])
        total += int(data["quantity"]) * int(data["price"])
    line = input()

print("Bought furniture:")
if furnit:
    print("\n".join(furnit))
print(f"Total money spend: {total:.2f}")
