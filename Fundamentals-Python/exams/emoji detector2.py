import re
import math
text = input()

sum_cool = math.prod([int(n) for n in text if n.isdigit()])
print(f'Cool threshold: {sum_cool}')

pattern = r"(::|\*\*)[A-Z][a-z][a-z]+\1"
emojies = re.finditer(pattern, text)

cool_emoji = []
count = 0
for em in emojies:
    count += 1
    total_sum = sum([ord(x) for x in em.group()[2:-2]])
    if total_sum >= sum_cool:
        cool_emoji.append(em.group())

print(f'{count} emojis found in the text. The cool ones are:')
if cool_emoji:
    for f in cool_emoji:
        print(f)

