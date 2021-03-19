import re
text = input()
pattern = r"@[a-zA-Z]{3,}@@[a-zA-Z]{3,}@|#[a-zA-Z]{3,}##[a-zA-Z]{3,}#"
result = []

matches = re.findall(pattern, text)
if matches:
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")

for string in matches:
    l_word, r_word = re.split("@@|##", string)
    if l_word == r_word[::-1]:
        result.append(f"{l_word[1:]} <=> {r_word[:-1]}")

if not result:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(*result, sep=", ")
