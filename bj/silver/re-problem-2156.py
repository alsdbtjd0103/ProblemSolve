n=int(input())
grape=[]
for i in range(n):
    grape.append(int(input()))
    
d=[0 for _ in range(n)]
if n<4:
    if n==1:
        d[0]=grape[0]
    if n==2:
        d[0]=grape[0]
        d[1]=grape[0]+grape[1]
    if n==3:
        d[0]=grape[0]
        d[1]=grape[0]+grape[1]
        d[2]=max(grape[0]+grape[1],grape[0]+grape[2],grape[1]+grape[2])
    print(d[n-1])    
    
else:       
    d[0]=grape[0]
    d[1]=grape[1]+grape[0]
    d[2]=max(grape[0]+grape[2],grape[1]+grape[2],grape[0]+grape[1])
    for i in range(3,n):
        d[i]=max(d[i-1],d[i-3]+grape[i-1]+grape[i],d[i-2]+grape[i])
    print(d[n-1])