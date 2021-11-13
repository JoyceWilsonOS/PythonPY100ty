def func(list_):
    return len([i for i in list_ if i % 2 == 0])


if __name__ == "__main__":
    # Write your solution here
    print(func([1, 2, 3, 4, 5, 10]))
    pass
