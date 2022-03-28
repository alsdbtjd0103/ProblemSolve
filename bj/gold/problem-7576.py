# 처음에는 토마토가 처음에 두개 이상 있을 수 있다는 것을 간과하였다.
# 그리고 que에 이제 맨 처음에 존재하는 토마토들의 좌표를 넣는 것 까지는 확신했는데
# 이게 que의 특성 선입선출을 이용할 수 있다는 것을 몰랐다.
# que를 이용하면 걍 좌표만 넣어주면 모두가 한번씩 번갈아가면서 실행된다.
# 그리고 토마토가 하나 이상 있다고 했지 그게 익었다고는 안했다 그래서 2 1 00 들어오면 -1이 나와야함


from collections import deque
def bfs(graph,visited,que):
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    while que:
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and graph[nx][ny]==0:
                visited[nx][ny]=visited[x][y]+1
                graph[nx][ny]=1
                que.append((nx,ny))

        
    
m,n=map(int,input().split())
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))
    
que=deque([])
visited=[[0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        if data[i][j]==1:
            que.append((i,j))
        
bfs(data,visited,que)
maxnum=-99999
result=0
for i in visited:
    if max(i)>maxnum:
        maxnum=max(i)

loc=True
for i in range(n):
    for j in range(m):
        if data[i][j]==0:
            loc=False
if not loc:
    result=-1
else:
    result=maxnum
print(result)

