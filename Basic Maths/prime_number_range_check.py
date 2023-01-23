def prime_number_range(n):
    ans = [True]*(n+1)
    limit = int(n**.5)+1
    for i in range(2, limit):
        if ans[i] == True:
            for j in range(i+i, n+1, i):
                ans[j] = False
    print(ans)
    for i in range(2, len(ans)):
        if ans[i]:
            print(i)


prime_number_range(50)
