# line = input().split('.')
# ver = ''
# for i in line:
#     ver += i
# ver = int(ver) + 1
# n_ver = []
# for i in str(ver):
#     n_ver.append(i)
# print('.'.join(n_ver))

line = input().split('.')
ver = int(''.join(line)) + 1
print('.'.join(str(ver)))
