# 문제가 조금 잘 못 되어있는 것 같다.
# 최대M개를 고르라고 되어있으면 당연히 1~M이지 않을까
# 그래서 계속 안풀렸는데 답을보니 그냥m개를무조건 고르는 것으로 되어있다.
# 그리고 여기서 combination에대해 처음알았다.

from itertools import combinations
n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

house=[]
chicken=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            house.append((i,j))
        elif graph[i][j]==2:
            chicken.append((i,j))
result=[]
c=list(combinations(chicken,m))
for i in c:
    distance=0
    for h in house:
        hx,hy=h
        minnum=1e9
        for z in i:
            cx,cy=z
            minnum=min(minnum,abs(hx-cx)+abs(hy-cy))
        distance+=minnum
    result.append(distance)
print(min(result))
        
    
    
    
    
    
    
 
    
                

    
                
        
                
                
     
