from collections import deque
import copy
n,m,v=map(int,input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
visited=[False]*(n+1)
dfs_data=[]
bfs_data=[]
for i in range(m):
    x,y=map(int,input().split())
    graph[x][y]=1
    graph[y][x]=1    # 양방향이기 때문에 둘다 1로 바꿔야한다. 아니면 2->5 인식x
temp=copy.deepcopy(graph)

def dfs(graph,visited,start):
    visited[start]=True
    dfs_data.append(str(start))
    for i in range(n+1):
        if graph[start][i]==1 and visited[i]==False:
            dfs(graph,visited,i)
            
def bfs(graph,visited,start):
    que=deque([start])
    while que:
        node=que.popleft()
        if visited[node]==False:
            bfs_data.append(str(node))
        visited[node]=True
        for i in range(1,n+1):
            if graph[node][i]==1 and visited[i]==False:
                que.append(i)
                
dfs(graph,visited,v)
graph=temp
visited=[False]*(n+1)
bfs(graph,visited,v)
dfs_node=" ".join(dfs_data)    # join같은 경우, 리스트안의 문자열을 합치는 것이                                  기 때문에 append할 때 문자열로 변환해서 넣어야                                  한다.
bfs_node=" ".join(bfs_data)
print(dfs_node)
print(bfs_node)



        
            