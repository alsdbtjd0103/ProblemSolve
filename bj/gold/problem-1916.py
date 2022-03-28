import sys
import heapq
input=sys.stdin.readline
INF=1e9
n=int(input().rstrip())
m=int(input().rstrip())
graph=[[] for i in range(n+1)]
for i in range(1,m+1):
    x,y,w=map(int,input().rstrip().split())
    graph[x].append((w,y))
    
start_point,destination=map(int,input().rstrip().split())
distance=[INF for i in range(n+1)]
def djkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        w,x=heapq.heappop(q)
        if w>distance[x]:
            continue
        for nd, nx in graph[x]:
            cost=nd+distance[x]
            if cost<distance[nx]:
                distance[nx]=cost
                heapq.heappush(q,(cost,nx))
djkstra(start_point)
print(distance[destination])
            
            

