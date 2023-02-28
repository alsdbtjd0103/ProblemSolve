from collections import defaultdict
from collections import deque
import copy
def board_to_str(board):
    result=''
    for i in board:
        result+=''.join(i)
    return result

def str_to_board(str):
    result=[[],[],[]]
    for i in range(9):
        result[i//3].append(str[i])
    return result

board=[]
zero_x,zero_y=0,0
for i in range(3):
    
    board.append(list(input().split()))
    for j in range(3):
        if board[i][j]=='0':
            zero_x,zero_y=i,j
    
b_str =board_to_str(board)

que=deque([(b_str,zero_x,zero_y)])
target = '123456780'
dic = defaultdict(int)
dic[b_str]=1
dx=[1,0,-1,0]
dy=[0,1,0,-1]


while que:
    b,x,y = que.popleft()
    if b==target:
        break
    board_b = str_to_board(b)

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and ny>=0 and nx<3 and ny<3:
            temp_board = copy.deepcopy(board_b)
            temp_board[nx][ny],temp_board[x][y] = temp_board[x][y],temp_board[nx][ny]
            temp_str = board_to_str(temp_board)
            if dic[temp_str]==0:
                dic[temp_str]=dic[b]+1
                que.append((temp_str,nx,ny))
print(dic[target]-1)