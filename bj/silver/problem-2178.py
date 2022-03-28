from collections import deque    
def bfs(graph,visited,v):
    que=deque([v])
    while que:
        x,y=que.popleft()
        visited[x][y]=True
        for i in range(4):
            next_x=x+dx[i]
            next_y=y+dy[i]
            if 0<=next_x<n and 0<=next_y<m:
                if visited[next_x][next_y]==0 and graph[next_x][next_y]==1:
                    que.append((next_x,next_y))
                    visited[next_x][next_y]=visited[x][y]+1
    print(visited[n-1][m-1])
         
            
n,m=map(int,input().split())
maze=[]
for i in range(n):
    maze.append(list(map(int,input())))
dx=[1,0,-1,0]
dy=[0,1,0,-1]
visited=[[0]*m for _ in range(n)]
visited[0][0]=1

bfs(maze,visited,(0,0))



# 그냥 bfs문제인데 내가 구상한 bfs를 사용하니까 계속 시간 초과가 발생
# 아마도 visited[i]를 i까지의 최단거리를 저장하는 용도로 쓰지 않고
# visited는 그냥 방문 판별기, 그리고 check[x][y]로 저장해서 참조하는데에
# 오래걸리는 것 같다.
