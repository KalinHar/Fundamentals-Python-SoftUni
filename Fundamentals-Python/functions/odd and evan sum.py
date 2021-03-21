number = input()


def odd_evan_sum(num):
    odd_sum = 0
    evan_sum = 0
    for d in num:
        if int(d) % 2 == 0:
            evan_sum += int(d)
        else:
            odd_sum += int(d)
    result = 'Odd sum = ' + str(odd_sum) + ', Even sum = ' + str(evan_sum)
    return result


print(odd_evan_sum(number))
