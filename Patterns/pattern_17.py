n = int(input('enter a value: '))


def pattern_17(n):
    for i in range(1, n+1):
        s = 65
        for j in range(n-i):
            print(' ', end="")
        for j in range(i):
            print(chr(s), end="")
            s += 1
        s2 = s-2
        for j in range(i-1):
            print(chr(s2), end="")
            s2 -= 1
        print('')


pattern_17(n)
