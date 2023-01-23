def armstrong(n):
    temp = n
    ans = 0
    rem = 0
    l = len(str(n))
    while temp:
        rem = temp % 10
        ans += rem**l

        temp = temp//10

    return ans == n


print(armstrong(407))
