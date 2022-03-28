from collections import deque
def bfs(graph,visited,v,l,goal):
    que=deque([v])
    while que:
        x,y=que.popleft()
        if x==goal[0] and y==goal[1]:
            return visited[x][y]
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<l and 0<=ny<l and visited[nx][ny]==0:
                que.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1
    return visited[goal[0]][goal[1]]
        
    
    
t=int(input())
length=[]
knight=[]
goal=[]
dx=[-2,-1,1,2,2,1,-1,-2]
dy=[1,2,2,1,-1,-2,-2,-1]
answer=[]

for i in range(t):
    length.append(int(input()))
    a,b=map(int,input().split())
    knight.append((a,b))
    a,b=map(int,input().split())
    goal.append((a,b))

for i in range(t):
    board=[[0]*length[i] for _ in range(length[i])]
    visited=[[0]*length[i] for z in range(length[i])]
    result=bfs(board,visited,knight[i],length[i],goal[i])
    answer.append(result)

for i in answer:
    print(i)
    
# 이번에도 bfs를 할 때 check 리스트를 사용하면 시간이 초과된다.
# 그냥 앞으로 최단거리 찾을때는 visited를 이용해야할 것 같다.
# 그리고 main에서 저렇게 for문 많이 쓸 필요없이 for문 하나안에 받고 바로 bfs
# 실행하면 더 간결해질듯

