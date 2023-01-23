n = int(input('enter a value'))


def pattern_14(n):
    s = 65
    for i in range(1, n+1):

        for j in range(i):
            print(chr(s), end="")

        print('')
        s += 1


pattern_14(n)
