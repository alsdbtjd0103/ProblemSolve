n=int(input())
d=[(0,0)]
t=[0]
p=[0]
for i in range(n):
    a,b=map(int,input().split())
    t.append(a)
    p.append(b)

if t[1]<=1:
    d.append((t[1],p[1]))
else:
    d.append((0,0))
    
for i in range(2,n+1):
    
    
    
    
        