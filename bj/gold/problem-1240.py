# 첫째 줄에 노드의 개수 N과 거리를 알고 싶은 노드 쌍의 개수 M이 입력되고
# 다음 N-1개의 줄에 트리 상에 연결된 두 점과 거리(10,000 이하의 정수)를 입력받는다.
# 그 다음 줄에는 거리를 알고 싶은 M개의 노드 쌍이 한 줄에 한 쌍씩 입력된다.
from collections import deque
n,m = map(int,input().split())
tree=[[] for i in range(n+1)]
result=[]

for i in range(1,n):
    a,b,c=map(int,input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))


for i in range(m):
    a,target=map(int,input().split())
    que=deque([])
    que.append(a)
    visited = [-1]*(n+1)
    visited[a]=0
    while que:
        x=que.popleft()
        for node,distance in tree[x]:
            if visited[node]==-1:
                que.append(node)
                visited[node]=visited[x]+distance
    result.append(visited[target])
for r in result:
    print(r)
                
            
