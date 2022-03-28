def dfs(graph,v):
    visited[v]=True
    data.append(v)
    for i in range(w*h):
        if graph[v][i]==1 and visited[i]==False:
            dfs(graph,i)
            
    
answer=[]
dx=[-1,0,1,0,-1,-1,1,1]
dy=[0,1,0,-1,-1,1,1,-1]
while True:
    data=[]
    w,h=map(int,input().split())
    count=0
    sum_num=0
    graph=[[0]*(w*h) for _ in range(w*h)]
    island=[]
    visited=[False]*(w*h)
    if (w,h)==(0,0):
        break
    for i in range(h):
        island.append(list(map(int,input().split())))
        for j in island[i]:
            if j==1:
                sum_num+=1
            
    for x in range(h):
        for y in range(w):
            if island[x][y]==0:
                visited[x*w+y]=True
                continue
            for z in range(8):
                nx=x+dx[z]
                ny=y+dy[z]
                if 0<=nx<h and 0<=ny<w and island[nx][ny]==1:
                    if (x*w+y)!=(nx*w+ny):
                        graph[x*w+y][nx*w+ny]=1    
                        graph[nx*w+ny][x*w+y]=1 
    
                        
    for j in range(w*h):
        if visited[j]==False:
            if len(data)==sum_num:
                break
            dfs(graph,j)
            count+=1
    answer.append(count)

for i in answer:
    print(i)
    

# 파이썬이라서 recursion error 발생.
# 그냥 bfs 쓰거나 pypy3로 변환
# visited[]는 노드에 0번부터 w*h-1번까지 이름을 붙여서 만들었고
# graph는 이 노드에서 노드의 연결 관계를 나타낸다
# 따라서 이 노드들의 이름을 설정하기 위해서는 x*w+y를 이용하여 표현하였다.
# 이렇게하면
# 0 1 2 3
# 4 5 6 7
# 이런식으로 노드번호를 만들 수 있기 때문이다.
    
            
                
            
    
                    
            

        
    
    