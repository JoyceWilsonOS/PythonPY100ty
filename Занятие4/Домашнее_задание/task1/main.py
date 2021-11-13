def if_digits_the_same(some_int):
    some_int_str = str(some_int)
    some_int_list = [k for k in some_int_str]
    return some_int_list.count(some_int_str[0]) == len(some_int_str)


if __name__ == "__main__":
    # Write your solution here
    print(if_digits_the_same(11111))
    pass
