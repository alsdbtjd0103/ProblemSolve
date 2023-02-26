from itertools import combinations
import copy
def slide_down():
    global board
    temp=[[0 for i in range(m)]]
    for i in range(n):
        if i==n-1:
            break
        temp.append(board[i])
    board=temp

def is_finished():
    global board
    for b in board:
        if 1 in b:
            return False
    return True
    
n,m,d = map(int,input().split())
global board
board=[]

for i in range(n):
    board.append(list(map(int,input().split())))
original = copy.deepcopy(board)
archor = [i for i in range(m)]

coms = combinations(archor,3)
result=[]

for com in coms:
    board=copy.deepcopy(original)
    position = [(n,com[0]),(n,com[1]),(n,com[2])]
    ans=0
    while True:
        if is_finished():
            break
        shoot=[]
        for x,y in position:
            possible_attack=[]
            for i in range(n):
                for j in range(m):
                    z = abs(i-x)+abs(j-y)
                    if z<=d:
                        possible_attack.append((i,j,z))
            possible_attack.sort(key=lambda x:(x[2],x[1],-1*x[0]))
            for x,y,z in possible_attack:
                if board[x][y]==1:
                    shoot.append((x,y))
                    break
        shoot=list(set(shoot))
        
        for x,y in shoot:
            board[x][y]=0
            ans+=1
        
        slide_down()
    result.append(ans)
print(max(result))


            
        

