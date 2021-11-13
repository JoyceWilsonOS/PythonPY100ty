def func(list_):
    sr_arif = sum(list_) / len(list_)
    print(sr_arif)
    return [i - sr_arif for i in list_]


if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print(func(list_))