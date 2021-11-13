def func(n, m):
    return [i ** 2 for i in range(n, m) if i % 2 == 1]
    ...


if __name__ == "__main__":
    # Write your solution here
    n = 3
    m = 6
    print(func(n, m))
    pass
