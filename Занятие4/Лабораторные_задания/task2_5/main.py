def func(number):
    print(f'number {number}')
    if str(number) == str(number)[::-1]:
        print('натуральное число является палиндромом')
    else:
        print('натуральное число не является палиндромом')


if __name__ == "__main__":
    # Write your solution here
    number = 13531
    func(number)
    pass

