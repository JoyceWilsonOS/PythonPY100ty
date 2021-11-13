def get_dif_words_from_line(str_):
    words = str_.split()
    words_unique = list(filter(lambda x: words.count(x) == 1, words))
    for el in words_unique:
        print(el)


if __name__ == "__main__":
    get_dif_words_from_line('staats dfgdfg sdfsdf a a b b c')
    pass
