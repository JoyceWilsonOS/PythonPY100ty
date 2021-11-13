def list_sort(some_list):
    some_list.sort(key=abs, reverse=True)
    return some_list


if __name__ == "__main__":
    list_ = [1, 2, -3, 4]
    print(list_sort(list_))
    # assert to_list(a, b, c) == [a, b, c]