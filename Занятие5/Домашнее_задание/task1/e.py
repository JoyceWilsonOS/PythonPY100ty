def to_dict(**kwargs):
    return kwargs


if __name__ == "__main__":
    print(to_dict(dog="Brock", fish=["Larry", "Curly", "Moe"], turtle="Shelldon"))
    # assert all_eq(a, b, c) == [a, b, c]