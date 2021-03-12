popu = input().split(', ')
popu = [int(p) for p in popu]
minumum = int(input())
if sum(popu) < minumum * len(popu):
    print('No equal distribution possible')
elif sum(popu) == minumum * len(popu):
    popu = [minumum] * len(popu)
    print(popu)
else:
    diff = 0
    for i in range(len(popu)):
        if popu[i] < minumum:
            diff = minumum - popu[i]
            popu[i] = minumum
            for n in range(len(popu)):
                if popu[n] == max(popu):
                    popu[n] = max(popu) - diff
                    break
            diff = 0
    print(popu)
