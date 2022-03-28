n=int(input())
d=[0]*(n+1)
if n>1:
    d[0],d[1],d[2]=0,1,1
    for i in range(3,n+1):
        d[i]=d[i-1]+d[i-2]
    print(d[n])
else:
    if n==1:
        print(1)
    else:
        print(0)