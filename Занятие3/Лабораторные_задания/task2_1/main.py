def task(str1, str2, k):
    if str1[:k] == str2[:k]:
        print('ДА')
    else:
        print('НЕТ')


if __name__ == "__main__":
    task('122345', '123789', 3)

