rooms = int(input())
game = True
count_free = 0
for r in range(1, rooms + 1):
    chairs = input().split(' ')
    if len(chairs[0]) < int(chairs[1]):
        print(f"{int(chairs[1]) - len(chairs[0])} more chairs needed in room {r}")
        game = False
    else:
        count_free += (len(chairs[0]) - int(chairs[1]))
if game:
    print(f'Game On, {count_free} free chairs left')
