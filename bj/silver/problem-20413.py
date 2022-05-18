n=int(input())
s,g,p,d=map(int,input().split())
rank=list(input())
for i in range(len(rank)):
    if rank[i]=='B': rank[i]=0
    if rank[i]=='S': rank[i]=1
    if rank[i]=='G': rank[i]=2
    if rank[i]=='P': rank[i]=3
    if rank[i]=='D': rank[i]=4

grade = [0,s,g,p,d,1e9]
this=0
past=0
result=0
for i in range(len(rank)):
    past=this
    this = grade[rank[i]+1]-past-1
    if this>d:
        this=d
    result+=this

print(result)

