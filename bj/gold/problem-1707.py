import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

k=int(input())

def dfs(graph,visited,s,color):
    global ans
    visited[s]=color
    for g in graph[s]:
        if visited[g]==0:
            dfs(graph,visited,g,color+1)
        elif visited[g]%2==color%2:
            ans=False
        

def check(visited,n):
    for i in range(1,n+1):
        if visited[i]==0:
            return False
    return True
    

result=[]
for _ in range(k):
    v,e=map(int,input().split())
    graph=[[] for i in range(v+1)]
    visited=[0 for i in range(v+1)]
    global ans
    ans=True
    for i in range(e):
        u,v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1,v+1):
        if visited[i]==0 and ans:
            dfs(graph,visited,i,1)

    if ans:
        result.append('YES')
    else:
        result.append('NO')
    

for r in result:
    print(r)

