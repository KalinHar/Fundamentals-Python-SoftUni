def sign(a, b, c):
    if a == 0 or b == 0 or c == 0:
        res = 'zero'
    elif (a > 0 and b > 0 and c > 0) or \
            (a > 0 and b < 0 and c < 0) or \
            (a < 0 and b > 0 and c < 0) or \
            (a < 0 and b < 0 and c > 0):
        res = 'positive'
    else:
        res = 'negative'
    return res


x = float(input())
z = float(input())
y = float(input())
print(sign(x, y, z))