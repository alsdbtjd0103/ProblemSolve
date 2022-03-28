from collections import deque

def check(next_ball):
    x,y=next_ball
    if 0<=x<n and 0<=y<m:
        if board[x][y]!='#':
            return True
    return False

def move_ball(red,blue,dx,dy):    ##한 칸만 이동
    global loc
    global end
    # print('red: ',red,'blue: ',blue)
    # print('visited red: ',visited[red[0]][red[1]])
    change=True
    num=visited[red[0]][red[1]]+1
    while True:

        
        if (red in hole):
            while True:
                next_blue=(blue[0]+dx,blue[1]+dy)
                if check(next_blue):
                    if next_blue in hole:
                        end=True
                        return (red,blue)
                    else:
                        blue=next_blue
                else:
                    break
            if not end:
                loc=True
                return (red,blue)
        if visited[red[0]][red[1]]>=10:
            end=True
            return (red,blue)
                    
                    
        if not change:
            return (red,blue)
        change=False
        next_red=(red[0]+dx,red[1]+dy)
        next_blue=(blue[0]+dx,blue[1]+dy)
        
        if check(next_red) and (next_red!=blue):
            if next_red!=next_blue:
                visited[next_red[0]][next_red[1]]=num
                red=next_red
                change=True
                
            
        if check(next_blue) and (next_blue!=red or red==hole):
            blue=next_blue
            change=True
        
        

        
        

        
n,m=map(int,input().split())
board=[]
visited=[[-1]*m for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
loc=False
hole=[]
found=False
not_found=False
count=0
end=False
for i in range(n):
    board.append(list(input()))


for i in range(n):
    for j in range(m):
        if board[i][j]=='R':
            red=(i,j)
        elif board[i][j]=='B':
            blue=(i,j)
        elif board[i][j]=='O':
            hole.append((i,j))
            
            
def bfs(start):
    global found
    global not_found
    global count
    q=deque()
    q.append(start)
    while q:
        red,blue=q.popleft()
        for i in range(4):
            next_x=red[0]+dx[i]
            next_y=red[1]+dy[i]
            if 0<=next_x<n and 0<=next_y<m and visited[next_x][next_y]==-1:
                red,blue=move_ball(red,blue,dx[i],dy[i])
                if loc:
                    found=True
                    count=visited[red[0]][red[1]]
                    return
                if end:
                    not_found=True
                    return
                q.append((red,blue))
        if visited[red[0]][red[1]]>10:
            not_found=True
            return
            
visited[red[0]][red[1]]=0               
bfs((red,blue))
if not_found:
    print(-1)
elif found:
    print(count)

    