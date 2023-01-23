def gcd(n1, n2):

    if (n1 > n2):  # find smallest because common factor cannot be greater than the smallest number
        n1, n2 = n2, n1
    limit = int(n1**0.5)+1
    # as we are finding greatest common factor start from the max possible common factor
    for i in range(limit, 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            return i


print(gcd(9, 12))
