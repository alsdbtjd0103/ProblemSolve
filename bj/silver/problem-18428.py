from itertools import combinations

def check(graph,start):
    x,y=start
    loc=True
    for i in range(x,-1,-1):
        if graph[i][y]=='O':
            break
        if graph[i][y]=='T':
            loc=False
            break
    for i in range(x,n):
        if graph[i][y]=='O':
            break
        if graph[i][y]=='T':
            loc=False
            break
    for i in range(y,-1,-1):
        if graph[x][i]=='O':
            break
        if graph[x][i]=='T':
            loc=False
            break
    for i in range(y,n):
        if graph[x][i]=='O':
            break
        if graph[x][i]=='T':
            loc=False
            break
    return loc

n=int(input())
graph=[]
s=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
wall=[]
for i in range(n):
    graph.append(list(input().split()))
    
for i in range(n):
    for j in range(n):
        if graph[i][j]=='S':
            s.append((i,j))
        elif graph[i][j]=='X':
            wall.append((i,j))
            
w=list(combinations(wall,3))
for z in w:
    result=True
    a,b,c=z
    graph[a[0]][a[1]]='O'
    graph[b[0]][b[1]]='O'
    graph[c[0]][c[1]]='O'
    for i in s:
        x,y=i
        result=check(graph,(x,y))
        if not result:
            break
    if result:
        # for x in graph:
        #     print(x)
        # print('')
        break
    graph[a[0]][a[1]]='X'
    graph[b[0]][b[1]]='X'
    graph[c[0]][c[1]]='X'
if result:
    print('YES')
else:
    print('NO')