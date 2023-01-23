def pattern_8(n):
    for i in range(n, 0, -1):
        for j in range(n-i):
            print(' ', end="")
        for j in range(i):
            print('*', end="")
        for j in range(i-1):
            print('*', end="")

        print("")


n = int(input('Enter a value : '))
pattern_8(n)
