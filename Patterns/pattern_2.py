

def pattern_2(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end="")
        print('')


n = int(input('Enter a value : '))
pattern_2(n)
