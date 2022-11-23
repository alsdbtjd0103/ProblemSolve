from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
n,m,r=map(int,input().split())

edge=[[] for i in range(n+1)]
visited=[False for i in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    edge[u].append(v)
    edge[v].append(u)

for i in range(len(edge)):
    edge[i].sort()


result=defaultdict(int)
global cnt
cnt=0
def dfs(s):
    global cnt
    visited[s]=True
    cnt+=1
    result[s]=cnt
    for x in edge[s]:
        if not visited[x]:
            dfs(x)
    
dfs(r)
for i in range(1,n+1):
    print(result[i])
