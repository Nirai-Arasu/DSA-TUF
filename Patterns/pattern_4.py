def pattern_4(n):
    for i in range(n):
        for j in range(i+1):

            print(i+1, end="")

        print('')


5

n = int(input('Enter a value : '))
pattern_4(n)
