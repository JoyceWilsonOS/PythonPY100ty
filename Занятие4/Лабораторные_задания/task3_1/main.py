# TODO
def dict_frequanc_symb(word):
    return {i: word.count(word[i]) for i in range(len(word))}


def dict_frequanc_symb_replace_for_percentage(int_dict: dict) -> dict:
    all_sum_values = sum(int_dict.values())
    print(f'all_sum_values {all_sum_values}')
    return {k: i / all_sum_values for k, i in int_dict.items()}


if __name__ == "__main__":
    main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """
    word = 'laska'
    dict_ = {k: word.count(k) for k in word}
    print(dict_)
    print(dict_frequanc_symb(word))
    string = "G2miny"
    print(string)
    new_string = string.lower()
    print(new_string)
    if string[1].isalpha():
        print('letter')
    print(dict_frequanc_symb_replace_for_percentage(dict_))

