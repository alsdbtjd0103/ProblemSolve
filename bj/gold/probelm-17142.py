# 간과했던점은 입력이 들어올 때, 바이러스 위치 가능한 지점이 모두 2로 들어오기때문에 bfs를 돌릴때 graph가 0일때만 실행하는게아니라 1이 아닐때 모두 실행해야함
# 그리고 모두 퍼뜨리지 못할 경우도 생각했어야함
# 그리고 비활성 바이러스에 대해서 생각하지 못함
# 비활성 바이러스도 활성되어있지 않더라도 바이러스이기 때문에 모두 비활성으로 차있으면 0초라는 것을 간과
from collections import deque
from itertools import combinations
import copy
n,m=map(int,input().split())
graph=[]
visited=[[-1]*n for i in range(n)]
v_possible=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
for i in range(n):
    graph.append(list(map(int,input().split())))
temp_graph=copy.deepcopy(graph)
    
for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            v_possible.append((i,j))
            
virus=list(combinations(v_possible,m))

def bfs(graph,visited,virus_loc):
    q=deque()
    for i in virus_loc:
        q.append(i)
        visited[i[0]][i[1]]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny]==-1 and graph[nx][ny]!=1:
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))

                

                  
min_time=1e9
for v in virus:
    time=-2
    visited=[[-1]*n for i in range(n)]
    bfs(graph,visited,v)
    loc=True
    non=True
    for i in range(n):
        for j in range(n):
            if time<visited[i][j] and graph[i][j]==0:
                time=visited[i][j]
            if visited[i][j]==-1 and graph[i][j]!=1:
                loc=False
            if graph[i][j]==0:
                non=False
    if non:
        min_time=0
        break
    if min_time>time and loc:
        min_time=time

if min_time==1e9:
    print(-1)
else:
    print(min_time)
        
    