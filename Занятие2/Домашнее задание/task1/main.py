if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, 3, -1, 8, 6, 9]

    # предположим, что первый элемент в нашем списке минимальный
    min_value_index = 0
    min_value = list_[min_value_index]

    # TODO заменить на enumerate
    for ind, el in enumerate(list_):
        if el <= min_value:
            min_value_index = ind
            min_value = el



    print("Минимальный элемент =", min_value, "находится по индексу", min_value_index)
