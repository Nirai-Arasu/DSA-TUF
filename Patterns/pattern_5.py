def pattern_5(n):
    for i in range(n):
        for j in range(n-i-1, -1, -1):
            print('*', end="")
        print('')


n = int(input('Enter a value : '))
pattern_5(n)
