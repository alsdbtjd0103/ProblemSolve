# 다익스트라 알고리즘에서 특정한 두 노드를 무조건 지나는 방법은
# 시작부터 d1까지, d1부터 d2까지, d2부터 마지막 노드까지 다익스트라 세번 돌리고
# 시작부터 d2까지, d2부터 d1까지, d1뷰토 마지막 노드까지 세번 돌려서
# 최소값을 반환하면 된다.

# 이 문제에서는 갈 수 없으면 -1 반환인데 양방향 간선이기 때문에 djkstra(1)을 했을 때 distance가 INF가 아니면 어떻게든 도달할 수 있기 때문에
# 처음 djkstra(1)을 했을 때 INF인지 아닌지만 확인해주면된다.
import sys
import heapq

def djkstra(start):
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start))
    while q:
        w,x=heapq.heappop(q)
        if w>distance[x]:
            continue
        for nd,nx in graph[x]:
            cost=nd+distance[x]
            if cost<distance[nx]:
                distance[nx]=cost
                heapq.heappush(q,(cost,nx))
                
INF=1e9
input=sys.stdin.readline
n,e=map(int,input().rstrip().split())
graph=[[] for i in range(n+1)]
distance=[1e9 for i in range(n+1)]
for i in range(1,e+1):
    a,b,c=map(int,input().rstrip().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
d1,d2=map(int,input().rstrip().split())


temp=[]
temp2=[]
loc=True

while True:
    djkstra(1)
    if distance[d1]==INF or distance[d2]==INF or distance[n]==INF:
        loc=False
        break
    temp.append(distance[d1])
    distance=[1e9 for i in range(n+1)]

    djkstra(d1)
    temp.append(distance[d2])
    distance=[1e9 for i in range(n+1)]

    djkstra(d2)
    temp.append(distance[n])
    distance=[1e9 for i in range(n+1)]



    djkstra(1)
    temp2.append(distance[d2])
    distance=[1e9 for i in range(n+1)]

    djkstra(d2)
    temp2.append(distance[d1])
    distance=[1e9 for i in range(n+1)]

    djkstra(d1)
    temp2.append(distance[n])
    distance=[1e9 for i in range(n+1)]
    
    break
    
if loc:
    print(min(sum(temp),sum(temp2)))
else:
    print(-1)



    