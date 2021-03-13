text = input()
text = text.split('@')
jump = input()
moment_jmp = 0
while jump != 'Love!':
    jump = jump.split(' ')
    jmp = int(jump[1])
    if jmp + moment_jmp >= len(text):
        moment_jmp = 0
    else:
        moment_jmp += jmp
    text[moment_jmp] = int(text[moment_jmp]) - 2
    if text[moment_jmp] == 0:
        print(f"Place {moment_jmp} has Valentine's day.")
    elif text[moment_jmp] < 0:
        text[moment_jmp] = 0
        print(f"Place {moment_jmp} already had Valentine's day.")
    jump = input()
print(f"Cupid's last position was {moment_jmp}.")
count = 0
for t in text:
    if t != 0:
        count += 1
if count > 0:
    print(f"Cupid has failed {count} places.")
else:
    print("Mission was successful.")
