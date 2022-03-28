import sys
from collections import deque

def bfs(tree,visited,start):
    que=deque([start])
    visited[start]=True
    while que:
        parent=que.popleft()
        for i in tree[parent]:
            if not visited[i]:
                p_node[i]=parent
                que.append(i)
                visited[i]=True
        
    
input=sys.stdin.readline
n=int(input().rstrip())
tree=[[] for i in range(n+1)]
visited=[False for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().rstrip().split())
    tree[a].append(b)
    tree[b].append(a)
    
p_node=[0 for i in range(n+1)]
bfs(tree,visited,1)
for i in range(2,len(p_node)):
    print(p_node[i])
