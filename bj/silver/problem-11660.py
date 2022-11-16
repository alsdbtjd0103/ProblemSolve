import sys
input=sys.stdin.readline
n,m=map(int,input().split())
board=[]
dp=[[0 for i in range(n+1)] for j in range(n+1)]

for i in range(n):
    board.append(list(map(int,input().split())))
    for k in range(len(board[i])):
        dp[i+1][k+1] = dp[i+1][k]+board[i][k]


result=[]
for i in range(m):
    a,b,c,d=map(int,input().split())
    ans=0

    for j in range(a,c+1):
        ans+=dp[j][d]-dp[j][b-1]

    result.append(ans)
    
for r in result:
    print(r)

