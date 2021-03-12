trace = input().split(' ')
trace = [int(x) for x in trace]
n = int(len(trace) / 2)
racer_l = 0
racer_r = 0
for i in range(0, n):
    if trace[i] == 0:
        racer_l *= 0.8
    else:
        racer_l += trace[i]
    if trace[-(i + 1)] == 0:
        racer_r *= 0.8
    else:
        racer_r += trace[-(i + 1)]
if racer_l < racer_r:
    print(f'The winner is left with total time: {racer_l:.1f}')
else:
    print(f'The winner is right with total time: {racer_r:.1f}')
