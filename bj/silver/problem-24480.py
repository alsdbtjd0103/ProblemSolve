import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
n,m,r=map(int,input().split())
visited=[False for i in range(n+1)]
graph=[[] for i in range(n+1)]

for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in range(len(graph)):
    graph[g].sort(reverse=True)


result=defaultdict(int)

global cnt
cnt=0

def dfs(s):
    global cnt
    visited[s]=True
    cnt+=1
    result[s]=cnt
    for x in graph[s]:
        if not visited[x]:
            dfs(x)
dfs(r)
for i in range(1,n+1):
    print(result[i])
    
