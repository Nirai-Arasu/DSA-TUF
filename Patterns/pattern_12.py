def pattern_12(n):
    for i in range(1, n+1):

        for j in range(1, i+1):
            print(str(j)+' ', end="")
        for j in range(n-i):
            print(" ", end="")
        for j in range(n-i):
            print("  ", end="")
        c = i
        for j in range(i):

            print(" "+str(c), end="")
            c -= 1
        print("")


n = int(input('enter : '))
pattern_12(n)
