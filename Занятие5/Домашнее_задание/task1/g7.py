def search_substr(subst, st):
    if subst.lower() in st.lower():
        print(f'Есть контакт!')
    else:
        print(f'Мимо!')


if __name__ == "__main__":
    search_substr('ти', 'карТИнка')

    # assert change(list_) == [4, 2, 3, 1]