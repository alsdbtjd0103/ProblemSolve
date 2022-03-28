from collections import deque

r,c=map(int,input().split())
graph=[]
destination=(-1,-1)
start=(-1,-1,True)
water=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
for i in range(r):
    graph.append(list(input()))

for i in range(r):
    for j in range(c):
        if graph[i][j]=='D':
            destination=(i,j)
        elif graph[i][j]=='S':
            start=(i,j,True)
        elif graph[i][j]=='*':
            water.append((i,j,False))

visited=[[-1]*c for _ in range(r)]

def bfs(graph,visited,start):
    q=deque()
    for i in water:
        q.append(i)
    q.append(start)
    visited[start[0]][start[1]]=0
    while q:
        x,y,z=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c and visited[nx][ny]==-1:
                if z:
                    if graph[nx][ny]=='.':
                        visited[nx][ny]=visited[x][y]+1
                        graph[nx][ny]='S'
                        q.append((nx,ny,z))
                    elif graph[nx][ny]=='D':
                        visited[nx][ny]=visited[x][y]+1
                        return True
                elif not z:
                    if graph[nx][ny]=='.':
                        visited[nx][ny]=visited[x][y]+1
                        graph[nx][ny]='*'
                        q.append((nx,ny,z))
                    elif graph[nx][ny]=='S':
                        return False
result=bfs(graph,visited,start)
if result:
    print(visited[destination[0]][destination[1]])
else:
    print('KAKTUS')
                        
                
    
        
    
        