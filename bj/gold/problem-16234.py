# pypy3로 해야만 시간 초과가 안난다.
# 이걸 줄일수 있는 방법은?
# 1. 함수호출시간을 줄이기 위해 bfs 함수를 없애고 직접 집어넣음
# ㄴ 해봤는데 그대로 시간초과.. 왜나는거양

from collections import deque
def bfs(graph,visited,start):
    que=deque([])
    que.append(start)
    temp=[]
    while que:
        x,y=que.popleft()
        visited[x][y]=True
        temp.append((x,y))
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and l<=abs(graph[x][y]-graph[nx][ny])<=r:
                que.append((nx,ny))
                visited[nx][ny]=True
    union.append(temp)
                    
            
n,l,r=map(int,input().split())
town=[]
union=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
num=0
visited=[[False]*n for i in range(n)]
for i in range(n):
    town.append(list(map(int,input().split())))
    
while True:
    visited=[[False]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(town,visited,(i,j))

    if len(union)==n*n:
        break
    for u in union:
        people=0
        for p in u:
            people+=town[p[0]][p[1]]
        people=people//len(u)
        for x,y in u:
            town[x][y]=people
    num+=1
    union=[]
print(num)
            
            

    

    