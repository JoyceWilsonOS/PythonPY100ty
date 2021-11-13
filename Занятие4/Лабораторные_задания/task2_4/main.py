def func(number):
    list_digits = [int(i) for i in str(number)]
    if sum(list_digits) % 7 == 0:
        print('сумма цифр числа кратна 7')
    else:
        print('сумма цифр числа не кратна 7')


if __name__ == "__main__":
    # Write your solution here
    number = 7331
    func(number)
    pass
