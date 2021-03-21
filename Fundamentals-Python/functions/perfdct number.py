num = int(input())


def perfect(number):
    sum_of_div = 0
    if number > 0:
        for n in range(1, number):
            if number % n == 0:
                sum_of_div += n
        if sum_of_div == number:
            print('We have a perfect number!')
        print("It's not so perfect.")
    print("It's not so perfect.")


perfect(num)
