# 그냥 bfs로는 불가능함 시간초과 발생
# 만약 1번벽에서 bfs를 돌렸을 때, 2번벽이랑 부딪혔다는 소리는
# 2번벽도 1번벽이 지나온 길을 갈 수 있다는 뜻
# 이걸 이용하면 될듯

from collections import deque
import sys
import copy

input=sys.stdin.readline
n,m=map(int,input().rstrip().split())
graph=[]
wall=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
for i in range(n):
    graph.append(list(map(int,input().rstrip())))
result=copy.deepcopy(graph)
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            wall.append((i,j))
visited=[[False]*m for i in range(n)]

def bfs(start):
    count=1
    q=deque()
    q.append(start)
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny]==0:
                visited[nx][ny]=True
                q.append((nx,ny))
                count+=1
    return count%10


for w in wall:
    visited=[[0]*m for i in range(n)]
    visited[w[0]][w[1]]=True
    c=bfs(w)
    result[w[0]][w[1]]=c
    
    
for i in result:
    for j in i:
        print(j,end='')
    print('')
    
        
    