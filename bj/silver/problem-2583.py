from collections import deque
m,n,k=map(int,input().split())
graph=[[0]*n for i in range(m)]
visited=[[0]*n for i in range(m)]
dx=[1,0,-1,0]
dy=[0,-1,0,1]
for i in range(k): ## 이걸 생각하는게 어려웠다.. 결국 검색을 통해 해결
    x,y,z,r=map(int,input().split())
    for j in range(y,r):
        for k in range(x,z):
            graph[j][k]=1


def bfs(start):
    q=deque()
    q.append(start)
    visited[start[0]][start[1]]=1
    num=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and visited[nx][ny]==0 and graph[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1
                num+=1
    return num

count=0
result=[]

for i in range(m):
    for j in range(n):
        if graph[i][j]==0 and visited[i][j]==0:
            result.append(bfs((i,j)))
            count+=1

print(count)
result.sort()
for i in result:
    print(i,end=' ')
            
            
        