n = int(input('enter a value : '))


def pattern_22(n):
    for i in range(n, 0, -1):
        start = n

        for j in range(n):
            print(start, end="")
            if start > i:
                start -= 1

        for j in range(1, n):
            if start < n and start <= j:
                start += 1
            print(start, end="")

        print('')
    for i in range(2, n+1):
        start = n
        for j in range(n):
            print(start, end="")
            if start > i:
                start -= 1
        for j in range(1, n):
            if start < n and start <= j:
                start += 1
            print(start, end="")
        print('')


pattern_22(n)
