if __name__ == "__main__":
    cart = {
        "apple": 80,
        "orange": 65,
        "banana": 40
    }
    sm_ = 0
    # TODO посчитать через ключи
    for fruit in cart:
        sm_ += cart[fruit]
        print(cart[fruit])  # получаем значение по ключу
    print(sm_)

    sm_ = 0
    for fruit in cart.values():
        sm_ += fruit
        print(fruit)
    print(sm_)
    # TODO посчитать через метод values
