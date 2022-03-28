# sys import 안하면 시간초과
# 계속헤맨 이유: djkstra(s)로해야하는데 djkstra(1)로해서

import heapq
import sys
input=sys.stdin.readline
def djkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        d,s=heapq.heappop(q)
        if distance[s]<d:
            continue
        for i in graph[s]:
            x_d,x=i
            nd=x_d+distance[s]
            if nd<distance[x]:
                distance[x]=nd
                heapq.heappush(q,(nd,x))
        
            
        
                
INF=1e9
v,e=map(int,input().rstrip().split())
graph=[[]*v for _ in range(v+1)]
distance=[INF]*(v+1)
k=int(input())
for i in range(e):
    x,y,z=map(int,input().rstrip().split())
    graph[x].append((z,y))
    
if v==1:
    print(0)
else:
    djkstra(k)
    for i in range(1,v+1):
        if distance[i]==INF:
            print('INF')
        else:
            print(distance[i])



    



    
    