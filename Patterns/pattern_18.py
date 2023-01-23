n = int(input('enter a value : '))


def pattern_18(n):

    for i in range(1, n+1):
        s = 65+n-1
        for j in range(i):
            print(chr(s), end=" ")
            s -= 1
        for j in range(n-i):
            print(' ', end="")
        print("")


pattern_18(n)
