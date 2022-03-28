n=int(input())
graph=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]

visited=[[False]*n for _ in range(n)]
for i in range(n):
    graph.append(list(map(int,input())))
result=[]
num=0
def dfs(graph,visited,v):
    global num;
    x,y=v
    if 0>x or x>=n or y>=n or y<0:
        return False
    if graph[x][y]==1 and not visited[x][y]:
        visited[x][y]=True
        num+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            dfs(graph,visited,(nx,ny))
        return True
    return False

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j]==1:
            dfs(graph,visited,(i,j))
            result.append(num)
            num=0
result.sort()
print(len(result))
for i in result:
    print(i)

    

            

    

    