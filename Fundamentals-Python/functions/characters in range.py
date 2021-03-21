first = input()
second = input()


def char_in_range(start, stop):
    for i in range(ord(start)+1, ord(stop)):
        print(chr(i), end=' ')


char_in_range(first, second)
