from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
board=[]
goal=0
for i in range(n):
    temp=list(map(int,input().split()))
    board.append(temp)
    if goal==0:
        for j in range(len(temp)):
            if temp[j]==2:
                goal=(i,j)

visited=[[-1 for i in range(m)] for j in range(n)]
que=deque([goal])
dx=[-1,0,1,0]
dy=[0,1,0,-1]
visited[goal[0]][goal[1]]=0

while que:
    x,y=que.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if ny>=0 and nx>=0 and nx<n and ny<m and visited[nx][ny]==-1 and board[nx][ny]==1:
            que.append((nx,ny))
            visited[nx][ny]=visited[x][y]+1

for i in range(n):
    for j in range(m):
        if visited[i][j]>=0:
            print(visited[i][j],end=' ')
        else:
            if visited[i][j]==-1 and board[i][j]==0:
                print(0,end=' ')
            else:
                print(-1,end=' ')
    print('')


