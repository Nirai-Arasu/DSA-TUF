def print_all_divisions(n):

    limit = int(n**.5)+1

    for i in range(1, limit):
        if n % i == 0:
            print(i)
            if i != n//i:
                print(n//i)


print_all_divisions(36)
