import sys
sys.setrecursionlimit(10**5)

input=sys.stdin.readline
board=[]
global found
found=False
for i in range(9):
    board.append(list(map(int,input().split())))

need=[]
for x in range(9):
    for y in range(9):
        if board[x][y]==0:
            need.append((x,y))

def check_xy(x,y,num):
    for i in range(9):
        if board[x][i]==num:
            return False
        if board[i][y]==num:
            return False
    temp_x,temp_y=(x//3)*3,(y//3)*3
    for i in range(temp_x,temp_x+3):
        for j in range(temp_y,temp_y+3):
            if board[i][j]==num:
                return False
    return True

def check_finish():
    for i in board:
        if 0 in i:
            return False
    
    return True

def dfs(num):
    global found
    if check_finish() and not found:
        for i in board:
            for j in i:
                print(j,end=' ')
            print('')
        found=True
        return
    if not found and len(need)>num:
        x,y=need[num]
        for i in range(1,10):
            if not check_xy(x,y,i):
                continue
            if not found:
                board[x][y]=i
                dfs(num+1)
                board[x][y]=0

dfs(0)





