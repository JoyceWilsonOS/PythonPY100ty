def func(list_):
    num_ch = [i for i in list_ if i % 2 == 0]
    print(f'num_ch, {num_ch}')
    num_nech = [i for i in list_ if i % 2 != 0]
    print(f'num_nech, {num_nech}')
    return 'even' if len(num_ch) > len(num_nech) else 'odd' if len(num_ch) < len(num_nech) else 'equal quantity'


if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print(func(list_))
