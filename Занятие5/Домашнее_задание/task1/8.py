def first_last(letter, st):
    fst = lst = None
    if letter.lower() in st.lower():
        fst = st.index(letter.lower())
        lst = st.rindex(letter.lower())
    return fst, lst


if __name__ == "__main__":
    print(first_last('А', 'карТИнк'))
    # assert change(list_) == [4, 2, 3, 1]


def first_last(letter, st):
    if letter not in st:
        return None, None
    first_index = st.index(letter)
    st = st[::-1]
    last_index = len(st) - st.index(letter) - 1
    return first_index, last_index


assert first_last(2, [2, 2, 5, 0, 3, 1]) == (0, 1)
