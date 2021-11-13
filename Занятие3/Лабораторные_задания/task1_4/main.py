def infinity(epsilon=0.0001):
    infinity_list = []
    n = 2

    while True:
        i = 1/n
        if i > epsilon:
            infinity_list.append(i)
            n *= 2
        else:
            break

    return sum(infinity_list)


def sum_(n):
    epsilon = 0.0001
    if 1/n < epsilon:
        return 1/n
    else:
        return 1/n + sum_(n*2)


if __name__ == "__main__":
    print(sum_(2))
    print(infinity())
    pass
