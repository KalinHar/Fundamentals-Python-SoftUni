string = input()
game = string.split(' ')
count_a = 11
count_b = 11
for g in game:
    if 'A' in g:
        count_a -= 1
    else:
        count_b -= 1
    if count_b < 7 or count_a < 7:
        break
print(f'Team A - {count_a}; Team B - {count_b}')
if count_b < 7 or count_a < 7:
    print('Game was terminated')
