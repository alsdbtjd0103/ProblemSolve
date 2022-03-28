import sys
sys.setrecursionlimit(100000)
n=int(input())
graph=[]
Max=-1
dx=[1,0,-1,0]
dy=[0,1,0,-1]
result=[]
visited=[[False]*n for _ in range(n)]

for i in range(n):
    graph.append(list(map(int,input().split())))
    if Max<max(graph[i]):
        Max=max(graph[i])
        
def dfs(x,y,h):
    for i in range(4):
        nx=x+dx[i]
        ny=y=dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny]<=h and not visited[nx][ny]:
                visited[nx][ny]=True
                dfs(nx,ny,h)
                
def dfs2(x,y,h):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny]>h and not visited[nx][ny]:
                visited[nx][ny]=True
                dfs2(nx,ny,h)
                
def check(h):
    count=0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j]>h:
                visited[i][j]=True
                dfs2(i,j,h)
                count+=1
    return count
            
            
for h in range(0,Max):
    for i in range(n):
        for j in range(n):
            if graph[i][j]<=h and not visited[i][j]:
                visited[i][j]=True
                dfs(i,j,h)
    c=check(h)
    visited=[[False]*n for _ in range(n)]
    result.append(c)

print(max(result))
            
    