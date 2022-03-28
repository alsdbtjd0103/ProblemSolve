t=int(input())
result=[]
for i in range(t):
    n,m=map(int,input().split())
    d=[0]*(m+1)
    d[1]=1
    if n==0:
        result.append(0)
        continue
    if m==1 or m==n:
        result.append(1)
        continue
        
    for i in range(2,m+1):
        d[i]=d[i-1]*i
    result.append((d[m]//d[m-n])//d[n])
    
    
for i in result:
    print(i)