def get_positive_sum(list_):
    sum_ = 0
    for el in list_:
        if el != 0:
            if el > 0:
                sum_ += el
        else:
            break
    return sum_


if __name__ == "__main__":
    print(get_positive_sum([1, 2, 3, -4, 5, -2, 0]))
    pass
