## 시간제한이 1초길래 통과못할줄 알았는데 이게 통과하네;;
## 그냥 각 노드에서 다 djkstra 돌려서 목표 노드까지의 최단거리 저장하고
## 목표노드 x에서 다시 다익스트라 한번 돌려서 각 노드에 더해줌

import sys
import heapq
input=sys.stdin.readline
INF=1e9
n,m,x=map(int,input().rstrip().split())
graph=[[] for i in range(n+1)]
for i in range(1,m+1):
    a,b,t=map(int,input().rstrip().split())
    graph[a].append((t,b))
    
distance=[INF for _ in range (n+1)]
d=[INF for _ in range(n+1)]

def djkstra(start):
    q=[(0,start)]
    distance[start]=0
    while q:
        dist,s=heapq.heappop(q)
        if dist>distance[s]:
            continue
        for i in graph[s]:
            nt,n_node=i
            cost=nt+distance[s]
            if cost<distance[n_node]:
                distance[n_node]=cost
                heapq.heappush(q,(cost,n_node))
result=[-1]
for i in range(1,n+1):
    djkstra(i)
    result.append(distance[x])
    distance=d[:]
    
djkstra(x)


for i in range(1,n+1):
    result[i]+=distance[i]
print(max(result))

    
    
    
                
            

            
    
    