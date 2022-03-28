# 주사위의 전개도를 계속 수정해주는게 어려웠다.
# 특히 오른쪽이나 왼쪽으로 굴릴 때, dice_y[1]=dice_x[2]처럼 하는게 포인트이다.
# 그리고 문제를 좀 더 정확히 읽어야할 것 같다. 보드에 숫자가 있으면 주사위에 대입하고 보드를 0으로
# 만들어주는 것을 넣지 않았었다.

from collections import deque

n,m,x,y,k=map(int,input().split())
board=[]
for i in range(n):
    board.append(list(map(int,input().split())))

move=deque(list(map(int,input().split())))
dice_y=deque([0,0,0,0])
dice_x=deque([0,0,0,0])
dxy=[(0,0),(0,1),(0,-1),(-1,0),(1,0)]

def check(nx,ny):
    if nx<0 or ny<0 or nx>n-1 or ny>m-1:
        return False
    return True

def moving_dice(nx,ny,direction):
    if direction==1:
        dice_x[0]=dice_y[3]
        temp=dice_x.pop()
        dice_x.appendleft(temp)
        dice_y[3],dice_y[1]=dice_x[0],dice_x[2]
        if board[nx][ny]==0:
            board[nx][ny]=dice_x[0]
        else:
            dice_y[3],dice_x[0]=board[nx][ny],board[nx][ny]
            board[nx][ny]=0
    if direction==2:
        dice_x[0]=dice_y[3]
        temp=dice_x.popleft()
        dice_x.append(temp)
        dice_y[3],dice_y[1]=dice_x[0],dice_x[2]
        if board[nx][ny]==0:
            board[nx][ny]=dice_x[0]
        else:
            dice_y[3],dice_x[0]=board[nx][ny],board[nx][ny]
            board[nx][ny]=0
    if direction==3:
        temp=dice_y.popleft()
        dice_y.append(temp)
        if board[nx][ny]==0:
            board[nx][ny]=dice_y[3]
        else:
            dice_y[3]=board[nx][ny]
            board[nx][ny]=0
        dice_x[0],dice_x[2]=dice_y[3],dice_y[1]
    if direction==4:
        #print("v")
        # print(f"(nx,ny): {(nx,ny)}\n board[nx][ny]: {board[nx][ny]}")
        temp=dice_y.pop()
        dice_y.appendleft(temp)
        if board[nx][ny]==0:
            board[nx][ny]=dice_y[3]
        else:
            dice_y[3]=board[nx][ny]
            board[nx][ny]=0
        dice_x[0],dice_x[2]=dice_y[3],dice_y[1]
        
result=[]     
while move:
    direction=move.popleft()
    nx,ny=x+dxy[direction][0],y+dxy[direction][1]
    if not check(nx,ny):
        continue
    moving_dice(nx,ny,direction)
    #show_dice()
    x=nx
    y=ny
    print(dice_y[1])
    
def show_dice():
    print("    "+str(dice_y[0]))
    for i in dice_x:
        print(i,end=" ")
    print("")
    print("    "+str(dice_y[2]))
    print("    "+str(dice_y[3]))
    if dice_y[1]!=dice_x[2]:
        print("dice_y: ",dice_y)
        print("dice_x: ",dice_x)
        print("error!!")
    

        
    
        
    



