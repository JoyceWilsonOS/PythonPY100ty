def count_months_using_provided_money(stipendia, rashody, inflyazia, nakoplenya):
    months = 0
    left_money = nakoplenya + stipendia - rashody
    if left_money >= 0:
        months += 1
    while left_money > 0:
        left_money = left_money + stipendia - rashody * inflyazia
        months += 1
    if months > 1:
        months -= 1
    elif months <= 0:
        months = 0
    return months


if __name__ == "__main__":
    nakoplenya = 49000
    stipendia = 1000
    rashody = 25000
    inflyazia = 1.05
    print(count_months_using_provided_money(stipendia, rashody, inflyazia, nakoplenya))
    pass
