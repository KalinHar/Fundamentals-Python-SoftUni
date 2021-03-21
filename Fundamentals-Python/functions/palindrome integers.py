text = input().split(', ')


def palindromes(integers):
    for num in integers:
        if num == num[::-1]:
            print(True)
        print(False)


palindromes(text)
