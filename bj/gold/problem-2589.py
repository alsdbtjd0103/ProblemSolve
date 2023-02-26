from collections import deque

def bfs(start,visited):
    que=deque([start])
    visited[start[0]][start[1]]=0
    while que:
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and ny>=0 and nx<n and ny<m and visited[nx][ny]==-1 and arr[nx][ny]=='L':
                que.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1
    ans = 0
    for v in visited:
        ans=max(ans,max(v))
    return ans
                



n,m=map(int,input().split())
arr=[]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
result=[]
for i in range(n):
    arr.append(list(input()))
for i in range(n):
    for j in range(m):
        if arr[i][j]=='W':
            continue
        visited=[[-1]*m for i in range(n)]
        ans=bfs((i,j),visited)
        result.append(ans)
print(max(result))


