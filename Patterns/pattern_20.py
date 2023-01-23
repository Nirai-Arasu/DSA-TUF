n = int(input('enter value : '))


def pattern_20(n):
    for i in range(1, n+1):
        for j in range(i):
            print('*', end="")
        for j in range(n-i):
            print(" ", end="")
        for j in range(n-i):
            print(" ", end="")
        for i in range(i):
            print('*', end="")
        print('')
    for i in range(n-1, -1, -1):
        for j in range(1, i+1):
            print('*', end="")
        for j in range(n-i):
            print(" ", end="")
        for j in range(n-i):
            print(" ", end="")
        for i in range(1, i+1):
            print('*', end="")
        print('')


pattern_20(n)
