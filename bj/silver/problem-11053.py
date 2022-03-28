n=int(input())
a=list(map(int,input().split()))
A=[0]
A=A+a
d=[1]*(n+1)
d[1]=1
for i in range(1,n+1):
    for j in range(1,i):
        if A[j]<A[i]:
            d[i]=max(d[i],d[j]+1)
print(max(d))
            
    
    
    
                    
        
        
