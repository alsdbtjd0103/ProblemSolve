from collections import deque
import copy

# 계속 틀렸다고 뜬 이유
# n>=10 정도로 큰 숫자로 했을 때 중간에 location에 자기자신이 들어가게 되면서
# 자기 자신으로 한번 더 이동하고, 그러면서 종료조건인 그전 위치와 현재 위치가 같아지게됨
# 그래서 중간에 끝나게되버림
# 정확히 왜 이렇게 들어가는지는 모르겠지만
# 그래서 location 안에 들어간 것 중 제일 거리가 짧고 위 왼쪽에 있는 것이
# 자기 자신이라면 pop하고 다시 location[0] 설정함으로써 해결

def check(x,y,graph):    ## 체크 함수
    if x<0 or y<0 or x>=n or y>=n:        
        return 0
    elif graph[x][y]>shark:
        return 0
    else:
        return 1
    
def bfs(graph,visited,start):  ##bfs탐색
    global shark_locate
    global timer
    global shark_eat
    nx=0
    ny=0
    location=[]
    que=deque([start])
    while que:
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if check(nx,ny,graph)==1:  ## 이동가능
                if visited[nx][ny]==0:  ## 방문한적없음녀
                    que.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1
                    if graph[nx][ny]<shark and 0<graph[nx][ny]:  ##그곳에 먹을 수 있는 먹이가 있으면
                        location.append((visited[nx][ny],nx,ny))  ##바로 위치 추가
    
    # print('-----------')
    # for _ in visited:
    #     print('|| ', _, ' ||')
    # print('-----------')  
    while True:
        if location:
            location.sort()
            if (location[0][1],location[0][2])==shark_locate: ## 자기자신이 location에 들어가있으면
                v=location.pop(0)
                continue
            graph[shark_locate[0]][shark_locate[1]]=0
            shark_locate=(location[0][1],location[0][2])
            graph[shark_locate[0]][shark_locate[1]]=9
            timer+=visited[shark_locate[0]][shark_locate[1]]
            shark_eat+=1
            break
        else:
            break
        # print('-----------')
        # for _ in graph:
        #     print('|| ', _, ' ||')
        # print('-----------')
        # print(shark_locate)
        # print('location: ',location)
        
        
dx=[-1,0,0,1]
dy=[0,-1,1,0]
graph=[]
shark=2
shark_eat=0
shark_locate=(0,0)
timer=0
n=int(input())
for i in range(n):
    graph.append(list(map(int,input().split())))
for a in range(n):
    for b in range(n):
        if graph[a][b]==9:
            shark_locate=(a,b)
            break

visited=[[0]*n for _ in range(n)]
temp2=copy.deepcopy(visited)
distance=[]

while True:
    x,y=shark_locate
    bfs(graph,visited,shark_locate)
    # print('shark: ',shark)
    if shark_locate==(x,y):
        print(timer)
        break
    else:
        if shark_eat==shark:
            shark+=1
            shark_eat=0
        visited=copy.deepcopy(temp2)
        

        