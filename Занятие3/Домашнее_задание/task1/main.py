def get_nums_from_interwal(list_of_nums):
    nums_needed = list(filter(lambda x: 3 <= x <= 13, list_of_nums))
    return nums_needed


if __name__ == "__main__":
    print(get_nums_from_interwal([1, 3, 16, 7, 13, 10, 2, -1]))
    pass
