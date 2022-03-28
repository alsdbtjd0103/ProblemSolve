#플로이드 알고리즘으로 하면 메모리 초과 발생
# 모든 노드에 대해 dfs를 돌리면 시간초과..어떻게 두번만 돌려서 해결하지
# 임의의 노드에서 가장 먼 노드까지의 거리와 그 먼 노드에서 dfs를 돌려서 나온 최대 거리 중 큰 값이 답
#why?? 잘 모름
#보니까 이제 맨처음 dfs에서는 가장 바깥에 있는 노드를 찾고 거기서 dfs를 한번더 돌리면 최대거리가 나올 수 밖에 없는 것 같다.

import sys
input=sys.stdin.readline
n=int(input().rstrip())
INF=1e9
tree=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for i in range(n):
    temp=list(map(int,input().rstrip().split()))
    v=temp[0]
    for j in range(1,len(temp),2):
        if temp[j]==-1:
            break
        tree[v].append((temp[j],temp[j+1]))

distance=[0]*(n+1)
def dfs(x):
    for y,d in tree[x]:
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
    
        
 