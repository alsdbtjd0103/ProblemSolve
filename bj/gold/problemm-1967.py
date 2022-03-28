# problem 1167과 똑같음 트리의 지름 구하기
import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline
n=int(input().rstrip())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
dx=[1,0,-1,0]
dy=[0,1,0,-1]

for i in range(n-1):
    a,b,c=map(int,input().rstrip().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance=[0]*(n+1)
def dfs(x):
    for y,d in graph[x]:
        if not visited[y]:
            distance[y]=distance[x]+d
            visited[y]=True
            dfs(y)
result=[]
visited[1]=True
dfs(1)
temp=0
for i in range(1,n+1):
    if distance[temp]<distance[i]:
        temp=i
result.append(distance[temp])
visited=[False]*(n+1)
distance=[0]*(n+1)
visited[temp]=True
dfs(temp)
result.append(max(distance))
print(max(result))


    

