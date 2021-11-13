def func(number):
    list_digits = [int(i) for i in str(number)]
    print(list_digits)
    sum_digits = sum(list_digits)
    print(sum_digits)
    number_digits = len(list_digits)
    print(number_digits)
    max_digit = max(list_digits)
    print(max_digit)
    list_odd_place_digits = [i for i in list_digits[1::2]]
    print(list_odd_place_digits)
    raz_1_last_digit = list_digits[0] - list_digits[-1]
    print(raz_1_last_digit)
    min_digit = min(list_digits)
    print(list_digits.index(min_digit))
    pass


if __name__ == "__main__":
    # Write your solution here
    number = 54321
    func(number)
    pass
