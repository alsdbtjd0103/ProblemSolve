from collections import deque
from collections import defaultdict
import sys
input=sys.stdin.readline

n,m,r=map(int,input().split())
visited=[False for i in range(n+1)]
graph=[[] for i in range(n+1)]
result=defaultdict(int)
for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(len(graph)):
    graph[i].sort(reverse=True)

def bfs(start):
    q=deque([])
    q.append(start)
    visited[start]=True
    result[start]=1
    cnt=1
    while q:
        x=q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i]=True
                cnt+=1
                result[i]=cnt
bfs(r)

for i in range(1,n+1):
    print(result[i])
    
