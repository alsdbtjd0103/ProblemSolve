n=int(input())
d=[0]*(n+1)
d[1]=1
if n==1:
    print(d[n])
elif n==2:
    d[2]=3
    print(d[n])
else:
    d[1]=1
    d[2]=3
    for i in range(3,n+1):
        d[i]=d[i-2]*2+d[i-1]
        d[i]=d[i]%10007
    print(d[n])
    
# (2x1 두개로 시작할경우+ 2x2하나로 시작할경우)+1x1로 시작할경우

