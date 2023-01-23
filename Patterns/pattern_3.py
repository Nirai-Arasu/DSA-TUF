def pattern_3(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end="")
        print('')


n = int(input('Enter a value : '))
pattern_3(n)
