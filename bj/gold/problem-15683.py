import sys
input=sys.stdin.readline
n,m=map(int,input().rstrip().split())
office=[]

for i in range(n):
    office.append(list(map(int,input().rstrip().split())))

cctv=[]
ans=1e9
for i in range(n):
    for j in range(m):
        if office[i][j]!=0 and office[i][j]!=6:
            cctv.append(office[i][j],i,j)

def func():
    

