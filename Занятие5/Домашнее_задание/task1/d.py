def all_eq(str_1):
    return [k.ljust(len(max(str_1)), '_') for k in str_1]


if __name__ == "__main__":
    str_ = ['sdf', 'd', 'sdfsdfsdf']
    print(str_)
    print(all_eq(str_))
    # assert all_eq(a, b, c) == [a, b, c]