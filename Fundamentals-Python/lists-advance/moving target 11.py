targets_sequence = [int(el) for el in input().split()]
initial_sequence_length = targets_sequence.copy()

while True:
    command = input().split()
    if command[0] == 'End':
        break
    if command[0] == 'Shoot':
        if 0 <= int(command[1]) < len(targets_sequence):
            targets_sequence[int(command[1])] -= int(command[2])
#REMOVER OF ZERO OR NEGATIVE ELEMENTS
            if targets_sequence[int(command[1])] <= 0:
                targets_sequence.remove(targets_sequence[int(command[1])])

    elif command[0] == 'Add':
        if 0 <= int(command[1]) < len(targets_sequence):
            targets_sequence.insert(int(command[1]), int(command[2]))
        else:
            print('Invalid placement!')

    elif command[0] == "Strike":
        target_index = int(command[1])
        radius = int(command[2])
        if radius + target_index < len(targets_sequence) and target_index - radius >= 0:
            # for targets in range(radius):
               # targets_sequence.remove(targets_sequence[target_index+1])
               # targets_sequence.remove(targets_sequence[target_index-1])
               # targets_sequence.remove(targets_sequence[target_index-1])
            targets_sequence = targets_sequence[:target_index - radius] + targets_sequence[target_index + radius + 1:]
        else:
            print('Strike missed!')

target_list = [str(el) for el in targets_sequence]
print("|".join(target_list))