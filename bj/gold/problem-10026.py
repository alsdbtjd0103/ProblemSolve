# 걍 bfs 두번 돌리니까 되넹;


from collections import deque

def bfs(graph,visited,start):
    que=deque()
    que.append(start)
    while que:
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False and graph[x][y]==graph[nx][ny]:
                que.append((nx,ny))
                visited[nx][ny]=True
                
                

n=int(input())
p=[]
p2=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
num=0
num2=0

for i in range(n):
    temp=list(input())
    p.append(temp)
    temp2=[]
    for j in temp:
        if j=='G':
            temp2.append('R')
        else:
            temp2.append(j)
    p2.append(temp2)


visited=[[False]*n for _ in range(n)]
visited2=[[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(p,visited,(i,j))
            num+=1
    
for i in range(n):
    for j in range(n):
        if not visited2[i][j]:
            bfs(p2,visited2,(i,j))
            num2+=1
print(num,num2)
            

                
            
