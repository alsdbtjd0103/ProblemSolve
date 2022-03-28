import sys
from itertools import combinations
from collections import deque
import copy

def check(board,start):
    que=deque([])
    que.append((0,start))
    while que:
        x,y=que.popleft()
        if board[x][y]==0:
            que.append((x+1,y))
        else:
            nx,ny=board[x][y]
            que.append((nx,ny))
        
        
    
    
input=sys.stdin.readline
n,m,h=map(int,input().rstrip().split())
graph=[[0]*n for _ in range(h)]
possible=[]
impossile_row=[]
for i in range(m):
    a,b=map(int,input().rstrip().split())
    graph[a-1][b-1]=(a-1,b)
    graph[a-1][b]=(a-1,b-1)
    impossible_row.append((a-1,b-1))
    impossible_row.append((a-1,b+1))
    


for i in range(h):
    for j in range(n):
        if graph[i][j]==0 and j!=(n-1):
            possible.append((i,j))
            
for i in range(1,4):
    com=list(combinations(possible,i))
    tmp=copy.deepcopy(graph)
    for c in com:
        for a,b in c:
            tmp[a][b]=(a,b+1)
            tmp[a][b+1]=(a,b)
        
        
            