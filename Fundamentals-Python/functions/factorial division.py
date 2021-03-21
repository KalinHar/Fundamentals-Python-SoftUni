a = int(input())
b = int(input())


def factoriel_div(first, second):
    import math
    f_sum = math.factorial(first)
    s_sum = math.factorial(second)
    # for f in range(2, first + 1):
    #     f_sum *= f
    # for s in range(2, second + 1):
    #     s_sum *= s
    print(f'{f_sum / s_sum:.2f}')


factoriel_div(a, b)
