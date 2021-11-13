def main():
    sum_ = 0
    num = 0
    while (sum_ := sum_ + num ** 2) <= 500:
        num += 1
    return num


if __name__ == "__main__":
    main()
