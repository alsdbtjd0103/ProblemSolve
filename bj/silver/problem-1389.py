from collections import deque

n,m=map(int,input().split())
p=[ [] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    p[a].append(b)
    p[b].append(a)

min_num=1e9
ans=0


for i in range(1,len(p)):
    num=0
    find_list=[0 for _ in range(n+1)]
    visited=[False]*(n+1)

    q=deque([i])
    while q:
        x=q.popleft()
        visited[x]=True
        for j in p[x]:
            if not visited[j]:
                q.append(j)
                find_list[j]=find_list[x]+1
                visited[j]=True


    num=sum(find_list)
    
    if num<min_num:
        ans=i
        min_num=num

print(ans)
            



