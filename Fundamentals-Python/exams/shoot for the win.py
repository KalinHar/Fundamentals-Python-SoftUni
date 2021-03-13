targets = [int(x) for x in input().split(' ')]
command = input()
shoots_counter = 0

while command != 'End':
    shoot = int(command)
    if 0 <= shoot < len(targets) and targets[shoot] != -1:
        points = targets[shoot]
        targets[shoot] = -1
        shoots_counter += 1
        for i in range(len(targets)):
            if targets[i] != -1:
                if targets[i] > points:
                    targets[i] -= points
                else:
                    targets[i] += points
    command = input()

print(f"Shot targets: {shoots_counter} -> {' '.join([str(x) for x in targets])}")
