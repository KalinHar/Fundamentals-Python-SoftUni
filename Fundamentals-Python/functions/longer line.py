import math


def close(x1, y1, x2, y2):
    res = None
    c1 = math.sqrt(x1 * x1 + y1 * y1)
    c2 = math.sqrt(x2 * x2 + y2 * y2)
    if c1 <= c2:
        res = f'({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})'
    else:
        res = f'({int(x2)}, {int(y2)})({int(x1)}, {int(y1)})'
    return res


def longer(xx1, yy1, xx2, yy2, xx3, yy3, xx4, yy4):
    xy12 = math.sqrt((xx1 - xx2) ** 2 +(yy1 - yy2) ** 2)
    xy34 = math.sqrt((xx3 - xx4) ** 2 +(yy3 - yy4) ** 2)
    if xy12 >= xy34:
        return close(xx1, yy1, xx2, yy2)
    else:
        return close(xx3, yy3, xx4, yy4)


a1 = float(input())
b1 = float(input())
c1 = float(input())
d1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())
d2 = float(input())
print(longer(a1, b1, c1, d1, a2, b2, c2, d2))
