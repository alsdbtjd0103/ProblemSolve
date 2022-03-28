from collections import deque
# import copy

#사과를 먹고 없애야한다.

n=int(input())
k=int(input())
board=[[0]*(n+1) for _ in range(n+1)]
snake=deque([])
snake.append((1,1))
dxy=[(0,1),(1,0),(0,-1),(-1,0)]
for i in range(k):
    x,y=map(int,input().split())
    board[x][y]=2
L=int(input())
direction=deque([])
for i in range(L):
    x,c=input().split()
    direction.append((int(x),c))
    

def end_check(next_position):
    nx,ny=next_position
    if next_position in snake:
        return True
    if nx<1 or ny<1 or nx>n or ny>n:
        return True
    return False

time,numdxy=0,0
location=(1,1)
while True:
    time+=1
    # print("time: ",time)
    x,y=location
    nx,ny=x+dxy[numdxy][0],y+dxy[numdxy][1]
    if end_check((nx,ny)):
        break
    if board[nx][ny]==0:
        snake.popleft()
        snake.append((nx,ny))
    elif board[nx][ny]==2:
        snake.append((nx,ny))
        board[nx][ny]=0
    location=(nx,ny)
    if direction and direction[0][0]==time:
        x,c=direction.popleft()
        if c=='L':
            numdxy-=1
            if numdxy<0:
                numdxy=3
        elif c=='D':
            numdxy+=1
            if numdxy>3:
                numdxy=0
    
    # temp_board=copy.deepcopy(board)
    # for i in snake:
    #     temp_board[i[0]][i[1]]='*'
    # for i in temp_board:
    #     print(i)
    # print("-----------------")
        

print(time)
        
    
    
    
    
                
        
    
    
    


    
    