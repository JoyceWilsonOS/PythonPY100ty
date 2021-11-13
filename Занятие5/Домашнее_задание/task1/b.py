def to_list(*args):
    list_ = [k for k in args]
    return list_


if __name__ == "__main__":
    a = 5
    b = 6
    c = 7
    print(to_list(a))
    # assert to_list(a, b, c) == [a, b, c]