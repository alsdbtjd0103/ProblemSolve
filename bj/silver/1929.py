m,n=map(int,input().split())
d=[True]*(n+1)
a=int(n**0.5)
for i in range(2,a+1):
    if d[i]==True:
        for j in range(i+i,n+1,i):
            d[j]=False

for i in range(m,n+1):
    if i==1:
        continue
    if d[i]==True:
        print(i)
    
        
##에라토스테네스의 체 검색하면 알 수 있음

    
        
        
    
    