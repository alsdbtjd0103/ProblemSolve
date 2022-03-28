n=int(input())
soldier=(list(map(int,input().split())))
count=n-len(set(soldier))
soldier=list(soldier)
soldier.insert(0,0)

if n==1:
    print(0)
elif n==2:
    if soldier[1]<soldier[2]:
        print(1)
    else:
        print(0)
else:
    d=[0 for _ in range(n+1)]
    if soldier[2]>soldier[1]:
        d[2]=1
    else:
        d[2]=0
    for i in range(3,n+1):
        if soldier[i]>soldier[i-1]:
            d[i]=min(d[i-2]+1,d[i-1]+1)
        else:
            d[i]=d[i-1]
            
print(d[n])
        
