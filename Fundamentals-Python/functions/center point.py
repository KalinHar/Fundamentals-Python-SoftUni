import math


def close(x1, y1, x2, y2):
    res = None
    c1 = math.sqrt(x1 * x1 + y1 * y1)
    c2 = math.sqrt(x2 * x2 + y2 * y2)
    if c1 <= c2:
        res = f'({int(x1)}, {int(y1)})'
    else:
        res = f'({int(x2)}, {int(y2)})'
    return res


a = float(input())
b = float(input())
c = float(input())
d = float(input())
print(close(a, b, c, d))