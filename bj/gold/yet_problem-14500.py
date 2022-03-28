def rotation(a):
    result=[]
    temp=[]
    for i in a:  ##맨처음 90도 회전
        x,y=i
        temp.append((y,x))
    result.append(temp)
    temp=[]
    for i in a: ##180회전
        x,y=i
        temp.append(())
        
        
    
        
    
maxnum=[]
n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

s1=[[(0,0),(0,1),(0,2),(0,3)],[(0,0),(1,0),(2,0),(3,0)]]
s2=[[(0,0),(0,1),(1,0),(1,1)]]
s3=[]
s4=[]
s5=[[(0,0),(0,1),(1,0),(0,-1)],[(0,0),(-1,0),(0,-1),(1,0)],[(0,0),(0,1),(-1,0),(0,-1)],[(0,0),(-1,0),(0,1),(1,0)]]

for i in range(5):
    maxn=-1
    for a in range(n):
        for b in range(m):
            r1=s
    

