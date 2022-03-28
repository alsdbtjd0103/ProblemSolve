from collections import deque
import sys

input=sys.stdin.readline
num=0
def bfs(start,visited):
    global num
    global d
    x,y=start
    visited[x][y]=True
    place[x][y]=2
    num+=1
    dir_4=0
    while True:
        if dir_4==4:
            nx=x+dx[(d+2)%4]
            ny=y+dy[(d+2)%4]
            if nx<0 or ny<0 or nx>=n or ny>=m or place[nx][ny]==1:
                break
            x,y=nx,ny
            dir_4=0
            continue
            
        search_num=(d+3)%4
        nx=x+dx[search_num]
        ny=y+dy[search_num]
        if nx>=0 and ny>=0 and nx<n and ny<m and not visited[nx][ny] and place[nx][ny]!=1:
            d=search_num
            x,y=nx,ny
            dir_4=0
            num+=1
            visited[nx][ny]=True
            place[nx][ny]=2
        else:
            d=search_num
            dir_4+=1
            
    
            
        
n,m=map(int,input().rstrip().split())
r,c,d=map(int,input().rstrip().split())
place=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
visited=[[False]*m for _ in range(n)]
for i in range(n):
    place.append(list(map(int,input().rstrip().split())))


bfs((r,c),visited)
print(num)
    
