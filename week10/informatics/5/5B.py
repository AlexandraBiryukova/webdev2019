def power(a,n):
    res=a
    p=1
    if n==0:
        return 1
    while(p < n):
        res *= a
        p += 1
    return res


a=float(input())
n=int(input())
print(power(a,n))