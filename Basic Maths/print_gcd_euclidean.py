def gcd(n1, n2):
    if (n1 > n2):
        n1 = n1 % n2
    else:
        n2 = n2 % n1
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1

    return gcd(n1, n2)


print(gcd(52, 10))


# [ greater % smaller ] => if one of the two no. is zero than other no.is the gcd
