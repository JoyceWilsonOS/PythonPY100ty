def count_money_for_year(stipendia, rashody, inflyazia, months):
    needed_money = rashody - stipendia
    for i in range(months-1):
        needed_money += int(rashody * inflyazia) - stipendia
    return needed_money

if __name__ == "__main__":
    stipendia = 1000
    rashody = 25000
    inflyazia = 1.03
    months = 10
    print(count_money_for_year(stipendia, rashody, inflyazia, months))
    # Write your solution here
    pass
