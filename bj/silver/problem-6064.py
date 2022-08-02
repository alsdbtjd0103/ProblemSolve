t=int(input())
for _ in range(t):
    m,n,x,y=map(int,input().split())
    flag=False
    while x<=m*n:
        if (x-y)%n==0:
            print(x)
            flag=True
            break
        x+=m
    if not flag:    print(-1)