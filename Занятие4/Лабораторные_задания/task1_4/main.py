def func(list_):
    sr_arif = sum(list_) / len(list_)
    print(sr_arif)
    return [i for i in list_ if i > sr_arif]


if __name__ == "__main__":
    # Write your solution here
    print(func([1, 2, 3, 4, 5, 10]))
    pass
