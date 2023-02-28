import sys
input=sys.stdin.readline

n,m = map(int,input().split())
board=[]
for i in range(n):
    board.append(list(map(int,input().split())))

dx=[1,0,-1,0]
dy=[0,1,0,-1]

answer=0

dp = [[-1 for i in range(m)] for j in range(n)]
def dfs(x,y):
    if x==n-1 and y==m-1:
        return 1
    if dp[x][y]!=-1:
        return dp[x][y]
    dp[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and ny>=0 and nx<n and ny<m:
            if board[nx][ny]<board[x][y]:
                dp[x][y]+=dfs(nx,ny)
    return dp[x][y]

if board[0][0]>board[n-1][m-1]:
    answer = dfs(0,0)
print(answer)
