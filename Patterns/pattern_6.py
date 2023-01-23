def pattern_6(n):
    for i in range(n):
        c = 1
        for j in range(n-i-1, -1, -1):

            print(c, end="")
            c += 1
        print('')


n = int(input('Enter a value : '))
pattern_6(n)
