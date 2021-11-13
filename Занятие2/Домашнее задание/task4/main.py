if __name__ == "__main__":
    # Write your solution here
    import random
    list_ = random.sample(range(10, 35), 10)
    print(list_)
    max_el_ind = 0
    max_el = list_[max_el_ind]
    for i in range(len(list_)):
        if list_[i] > max_el:
            max_el = list_[i]
            max_el_ind = i
    temp = list_[0]
    list_[0] = list_[max_el_ind]
    list_[max_el_ind] = temp
    print(list_)
    pass
