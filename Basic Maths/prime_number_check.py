def prime_number(n):
    if n <= 1:
        return False

    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            return False
    print(n)


for i in range(10):
    prime_number(i)

# A number with only two factors, one and itself, is a prime number.
