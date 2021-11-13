def simplifier(num: int) -> list:
    start = 2
    list_ = []
    while start <= num:
        if num % start == 0:
            list_.append(start)
            num /= start
        else:
            start += 1
    return list_


if __name__ == "__main__":
    print(simplifier(256))
    pass
