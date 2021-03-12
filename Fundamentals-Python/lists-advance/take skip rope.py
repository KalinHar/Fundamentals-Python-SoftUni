line = input()
nums = []
strings = []
for l in line:
    if "0" <= l <= "9":
        nums.append(int(l))
    else:
        strings.append(l)
res = []
count = 0
for n in range(len(nums)):
    if n % 2 == 0:
        for i in range(count, count + nums[n]):
            res.append(strings[i])
        count += nums[n]
    else:
        count += nums[n]
print(''.join(res))
