# 아직 잘 이해가 안된다.
# 우선 3차원 리스트를 이용해서 0일경우 아직 안부순거고 1일경우 이미 부숴서 도달한
# 최단 거리를 저장한다는 것 까지는 이해함.
# 근데 이게 정확히 어떻게 bfs가 돌아가는지 이해가 안된다..어지러
# 다음에 다시 풀어보자
from collections import deque
def bfs(graph,visited,start):
    que=deque([start])
    visited[0][0][0]=1
    while que:
        x,y,z=que.popleft()
        for i in range(4):
        
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==0 and visited[nx][ny][z]==0:
                    visited[nx][ny][z]=visited[x][y][z]+1
                    que.append((nx,ny,z))
                elif z==0 and graph[nx][ny]==1 and visited[nx][ny][z]==0:
                    visited[nx][ny][1]=visited[x][y][z]+1
                    que.append((nx,ny,1))
        

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,list(input()))))

dx=[-1,0,1,0]
dy=[0,1,0,-1]
visited=[[[0]*2 for i in range(m)] for i in range(n)]
v=(0,0,0)
bfs(graph,visited,v)
result1=visited[n-1][m-1][0]
result2=visited[n-1][m-1][1]
if result1==0 and result2!=0:
    print(result2)
elif result1!=0 and result2==0:
    print(result1)
elif result1==0 and result2==0:
    print(-1)
else:
    print(min(result1,result2))