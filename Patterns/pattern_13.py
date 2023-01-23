n = int(input('enter  :'))


def pattern_12(n):
    c = 0
    for i in range(1, n+1):

        for j in range(i):
            c += 1
            print(str(c)+' ', end="")

        print("")


pattern_12(n)
