text = input()
water = int(input())
result = text.split('#')
effort = 0
tot_fire = []
for i in range(len(result)):
    row = result[i].split(' = ')
    fire = int(row[1])
    if 'High' in result[i] and 81 <= fire <= 125 and water >= fire:
        tot_fire.append(fire)
        water -= fire
        effort += (fire * 0.25)
    elif 'Medium' in result[i] and 51 <= fire <= 80 and water >= fire:
        tot_fire.append(fire)
        water -= fire
        effort += (fire * 0.25)
    elif 'Low' in result[i] and 1 <= fire <= 50 and water >= fire:
        tot_fire.append(fire)
        water -= fire
        effort += (fire * 0.25)
    if water <= 0:
        break
if len(tot_fire) >= 1:
    print('Cells:')
    for t in tot_fire:
        print(f' - {t}')
    print(f'Effort: {effort:.2f}')
    print(f'Total Fire: {sum(tot_fire)}')
else:
    print('Cells:')
    print(f'Effort: 0.00')
    print(f'Total Fire: 0')