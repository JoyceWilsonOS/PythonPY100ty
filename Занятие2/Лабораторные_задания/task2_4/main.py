if __name__ == "__main__":
    # постарайтесь не использовать "магические" числа,
    # а по возможности дать переменным осмысленные названия и использовать их
    # TODO Распечатать строку лесенкой
    otstup = 5
    string_ = "Hello, World"

    for prob, letter in enumerate(string_):
        print(' ' * otstup + ' ' * prob + letter)
