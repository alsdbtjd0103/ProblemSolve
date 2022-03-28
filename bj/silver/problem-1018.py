# 이렇게 무식하게 하기보다는
# 이제 행+열이 짝수이면 시작점과의 색깔과 같아야하고 홀수이면 달라야한다는 사실을 이용하면 간단하게 가능

import sys

def cutting_board(node):
    x,y=node
    temp_board=[]
    first_white_num=0
    first_black_num=0
    f_w_pre='W'
    f_b_pre='B'
    for i in range(8):
        temp_board.append(board[x+i][y:y+8])
        
    
    for i in range(8): #첫번째가 W
        if i>0:
            if f_w_pre=='W':
                f_w_pre='B'
            else:
                f_w_pre='W'
        for j in range(8):
            if i==0 and j==0:
                if temp_board[i][j]!='W':
                    first_white_num+=1
            elif f_w_pre=='W':
                if temp_board[i][j]=='W':
                    first_white_num+=1
                f_w_pre='B'
            else:
                if temp_board[i][j]=='B':
                    first_white_num+=1
                f_w_pre='W'       
    for i in range(8): #첫번째가 B
        if i>0:
            if f_b_pre=='W':
                f_b_pre='B'
            else:
                f_b_pre='W'
        for j in range(8):
            if i==0 and j==0:
                if temp_board[i][j]!='B':
                    first_black_num+=1
            elif f_b_pre=='B':
                if temp_board[i][j]=='B':
                    first_black_num+=1
                f_b_pre='W'
            else:
                if temp_board[i][j]=='W':
                    first_black_num+=1
                f_b_pre='B'
    return min(first_white_num,first_black_num)


    
        
    
input=sys.stdin.readline
n,m=map(int,input().rstrip().split())
board=[]
for i in range(n):
    board.append(list(input().rstrip()))
result=[]
for i in range(0,n-7):
    for j in range(0,m-7):
        result.append(cutting_board((i,j)))
        
print(min(result))
    
    