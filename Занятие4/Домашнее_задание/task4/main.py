def if_num_is_lucky(some_int):
    first_sum = sum([int(i) for i in str(some_int)[:3]])
    last_sum = sum([int(i) for i in str(some_int)[3:]])
    return first_sum == last_sum


if __name__ == "__main__":
    # Write your solution here
    print(if_num_is_lucky(123123))
    pass
