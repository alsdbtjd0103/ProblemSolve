## dfs나 bfs 어떤걸로든 풀수 있긴하다. 그런데 여기서 포인트는
# visited 리스트를 쓰면 안된다는 것이다. 쓰더라도 기존에 쓰던 방식이
# 아닌 지나간 알파벳을 저장하는 용도로 사용해야한다.
# 그냥 obstacle=[]에 append하고 remove하는 방식으로는 시간초과가 나서
# 미리 리스트를 준비해놓고 찾는 식으로 하면 pypy3로 겨우 통과
import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
r,c=map(int,input().rstrip().split())
board=[]
for i in range(r):
    board.append(list(input().rstrip()))
visited=[[0]*(c) for _ in range(r)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
obstacle=[0 for _ in range(26)]
answer=0
def dfs(x,y,cnt):
    global answer
    answer=max(answer,cnt)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<r and 0<=ny<c:
            if obstacle[ord(board[nx][ny])-65]==0:
                obstacle[ord(board[nx][ny])-65]=1
                cnt+=1
                dfs(nx,ny,cnt)
                obstacle[ord(board[nx][ny])-65]=0
                cnt-=1


            
obstacle[ord(board[0][0])-65]=1
dfs(0,0,1)
print(answer)

    