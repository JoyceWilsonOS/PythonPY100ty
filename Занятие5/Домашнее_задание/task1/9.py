def more_than_five(lst):
    return [k for k in lst if abs(k) > 5]


if __name__ == "__main__":

    print(more_than_five([4, -6, 7, 1]))

    # assert change(list_) == [4, 2, 3, 1]
