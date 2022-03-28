import copy
from collections import deque
from itertools import combinations

def bfs(graph,visited,start): ##bfs로 각 바이러스부터 시작해서 퍼뜨림
    que=deque([])
    que.append(start)
    while que:
        x,y=que.popleft()
        visited[x][y]=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and graph[nx][ny]==0:    
                que.append((nx,ny))
                visited[nx][ny]=1
                graph[nx][ny]=2
        
        
    
    
n,m=map(int,input().split())
graph=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
visited=[[0]*m for i in range(n)]
for i in range(n):
    graph.append(list(map(int,input().split())))
    
not_walls=[]
virus=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            not_walls.append((i,j))
        elif graph[i][j]==2:
            virus.append((i,j))


nw=list(combinations(not_walls,3)) ## 벽 세개를 선택할 수 있는 모든 조합을 리스트에 저장
result=[]
for i in nw: ##각 조합별로
    temp=copy.deepcopy(graph)
    temp2=copy.deepcopy(visited)
    num=0
    for w in i: ## 그 조합안에 있는 좌표들(3개) 모두 1로 변환
        wx,wy=w
        temp[wx][wy]=1
    for v in virus:    #각 virus안에 있는 좌표들마다 bfs 돌려주기
        bfs(temp,temp2,v)
    for a in range(n):
        for b in range(m):
            if temp[a][b]==0:
                num+=1
    result.append(num)   

print(max(result))

    
                
    
    
    
    
    
    