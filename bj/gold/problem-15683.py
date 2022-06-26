n,m=int(input().split())
board=[]
cctv=[]
for i in range(n):
    board.append(list(map(int,input().split())))
    for j in range(m):
        if board[i][j]!=0:
            cctv.append((i,j))

