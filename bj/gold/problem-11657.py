n,m=map(int,input().split())
INF=1e9
graph=[[]*(n+1)]
distance=[[[INF]*(n+1) for _ in range(n+1)]]
distance[1][1]=0
for i in range(m):
    a,b,c=map(int,input().split())
    distance[a][b]=c
    graph[a].append(b)

for i in range(n):
    for node in graph:
        for neighbor in node:
            distance[neighbor]=min(distance[neighbor],distance[node]+)