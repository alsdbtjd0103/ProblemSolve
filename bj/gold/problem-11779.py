import sys
import heapq
INF=1e9
input=sys.stdin.readline
n=int(input().rstrip())
m=int(input().rstrip())
graph=[[] for i in range((n+1))]
for i in range(1,m+1):
    a,b,c=map(int,input().rstrip().split())
    graph[a].append((c,b))
start,destination=map(int,input().rstrip().split())
distance=[INF for i in range(n+1)]

path=[0 for _ in range(n+1)]

def djkstra(start):
    que=[(0,start)]    
    distance[start]=0
    path[1]=start
    while que:
        w,x=heapq.heappop(que)
        if w>distance[x]:
            continue
        for nd,nx in graph[x]:
            cost=nd+distance[x]
            if cost<distance[nx]:
                distance[nx]=cost
                heapq.heappush(que,(cost,nx))
                path[nx]=x
djkstra(start)
print(distance[destination])

temp=[]
temp.append(destination)

z=path[destination]
while True:
    if z==start or z in temp:
        break
    temp.append(z)
    z=path[z]

temp.append(start)
temp.reverse()
print(len(temp))

for i in range(len(temp)):
    if i!=len(temp)-1:
        print(temp[i],end=' ')
    else:
        print(temp[i])

            
            

        
    
    