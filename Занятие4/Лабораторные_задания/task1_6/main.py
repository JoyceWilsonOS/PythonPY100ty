def func(list_):
    return len([i for i in list_ if i > list_[0]])


if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print(func(list_))
