a = int(input())
b = int(input())
c = int(input())


def add_and_subtract(first, second, third):

    def sum_numbers(s_fi, s_se):
        return s_fi + s_se

    def subtract(sumata, s_th):
        return sumata - s_th

    return subtract(sum_numbers(first,second),third)


print(add_and_subtract(a,b,c))

