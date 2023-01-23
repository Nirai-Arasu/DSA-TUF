
def pattern_1(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print("")


n = int(input('Enter a value :'))

print(n)
pattern_1(n)
