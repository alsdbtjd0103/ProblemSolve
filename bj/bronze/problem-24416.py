
cnt=[0,0]
def fib1(n):
    if n==1 or n==2:
        cnt[0]+=1
        return 1
    else:
        return(fib1(n-1)+fib1(n-2))


def fib2(n):
    f=[0 for i in range(n+1)]
    f[1],f[2]=1,1
    for i in range(3,n+1):
        f[i]=f[i-1]+f[i-2]
        cnt[1]+=1
    return f[n]

a=int(input())
fib1(a)
fib2(a)
print(cnt[0],cnt[1])

