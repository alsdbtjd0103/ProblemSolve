import heapq

t=int(input())
while t>0:
    k=int(input())
    visited=[False]*1000001
    minh=[]
    maxh=[]
    op=[]
    for i in range(k):
        x,y=input().split()
        op.append((x,int(y)))
    
    for i in range(len(op))
        o,n=op[i]
        if o=='I':
            heapq.heappush(maxh,(-n,i))
            heapq.heappush(minh,(n,i))

        elif o=='D' and n==-1 and que:
            temp=heapq.heappop(minh)
        elif o=='D' and n==1 and que:
            temp=heapq.heappop(maxh)
        
    while 

    
    if que:
        que.sort()
        print(que[-1],que[0])
    else:
        print('EMPTY')
    
            
    
