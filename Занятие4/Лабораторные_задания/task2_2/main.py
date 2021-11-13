def func(number):
    list_digits = [int(i) for i in str(number)]
    if 4 in list_digits and 8 in list_digits or 9 in list_digits:
        print('входят 4 и 8 или цифра 9')
    else:
        print('не входят')


if __name__ == "__main__":
    # Write your solution here
    number = 89
    func(number)
    pass
