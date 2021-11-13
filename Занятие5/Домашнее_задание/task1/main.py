if __name__ == "__main__":
    num = 19

    ots = 6
    for i in range(num+1):
        if i > 0:
            print(str(i).rjust(ots), end="")
        else:
            print(' '.rjust(ots), end="")
    print()
    for i in range(num+1):
        if i == 0:
            print(':'.rjust(ots), end="")
        else:
            print(str('_'*ots).rjust(ots), end="")
    for row in range(num+1):
        for col in range(num+1):
            if row and col > 0:
                print(str(row*col).rjust(ots), end="")
            elif col == 0 and row > 0:
                print((str(row)+':').rjust(ots), end="")
        print()
