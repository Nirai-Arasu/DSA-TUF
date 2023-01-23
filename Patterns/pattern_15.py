n = int(input('enter a value'))


def pattern_14(n):

    for i in range(n, 0, -1):
        s = 65
        for j in range(i):
            print(chr(s), end="")
            s += 1
        print('')


pattern_14(n)
