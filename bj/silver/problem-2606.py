from collections import deque

def bfs(graph,visited,v):
    que=deque([v])
    count=0
    visited[v]=True
    while que:
        node=que.popleft()
        for i in range(1,n+1):
            if graph[node][i]==1 and visited[i]==False:
                que.append(i)
                visited[i]=True
                count+=1
    return count
                
            
    

n=int(input())
m=int(input())
graph=[[0]*(n+1) for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(m):
    x,y=map(int,input().split())
    graph[x][y]=1
    graph[y][x]=1
    
result=bfs(graph,visited,1)
print(result)

# 드디어 bfs할때 왜 계속 중복되는게 생겼는지 깨달음.
# visited[i]=True를 for문 안에 넣어야함. while바로 다음에 넣어버리면 for문 돌리는동안 겹치는 숫자들이 계속 추가되어버림.
    