import sys
input=sys.stdin.readline

def bfs(graph,visited, start)

n,m,k,x=map(int,input().rstrip().split())
graph=[[]*(n+1)]
for i in range(m):
    a,b=map(int,input().rstrip().split())
    graph[a].append(b)
    

    
    