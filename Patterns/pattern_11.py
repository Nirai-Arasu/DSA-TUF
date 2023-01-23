def pattern_11(n):
    for i in range(1, n+1):
        if (i % 2) == 0:
            c1 = 0
            c2 = 1
        else:
            c1 = 1
            c2 = 0
        for j in range(i):
            if (j % 2 == 0):
                print(str(c1)+" ", end="")
            else:
                print(str(c2)+" ", end="")
        print('')


n = int(input('enter a val : '))
pattern_11(n)
