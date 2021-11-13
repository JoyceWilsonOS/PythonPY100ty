def func(number):
    list_digits = [int(i) for i in str(number)]
    if 9 < sum(list_digits) < 100:
        print('сумма цифр числа - число двузначное')
    else:
        print('сумма цифр числа - число недвузначное')


if __name__ == "__main__":
    # Write your solution here
    number = 923
    func(number)
    pass