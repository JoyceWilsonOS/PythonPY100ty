def define_palindrome(str_):
    str_obr = str_[::-1]
    if str_ == str_obr:
        return True
    else:
        return False

if __name__ == "__main__":
    print(define_palindrome('staats'))
    pass
