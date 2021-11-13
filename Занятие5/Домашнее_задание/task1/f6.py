import random


def count_it(sequence: str) -> dict:
    return {int(el): sequence.count(el) for el in sequence}


if __name__ == "__main__":
    str_ = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    print(str_)
    n_dict = count_it(str_)
    print(n_dict)
    sort_ = sorted(n_dict.items(), key=lambda x: x[1], reverse=True)[:3]
    print(sort_)

    # assert change(list_) == [4, 2, 3, 1]