def change(some_list_):
    some_list_[0], some_list_[-1] = some_list_[-1], some_list_[0]
    return some_list_


if __name__ == "__main__":
    list_ = [1, 2, 3, 4]
    # print(change(list_))
    assert change(list_) == [4, 2, 3, 1]
