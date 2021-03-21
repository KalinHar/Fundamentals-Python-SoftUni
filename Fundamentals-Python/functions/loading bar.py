num = int(input())


def loading(bar):
    if bar == 100:
        print('100% Complete!')
        print('[%%%%%%%%%%]')
    else:
        percents = '%' * int(bar / 10)
        dots = '.' * (10 - len(percents))
        print(f'{bar}% [{percents}{dots}]')
        print("Still loading...")


loading(num)