import heapq
import sys
input=sys.stdin.readline
n=int(input())
q=[]
results=[]
for i in range(n):
    x=int(input())
    if x==0:
        if q:   
            temp=heapq.heappop(q)
            results.append(temp[1])
        else:   results.append(0)
    else:   heapq.heappush(q,(abs(x),x))

for r in results:
    print(r)
