n=int(input())
line=[]
for i in range(n):
    a,b=map(int,input().split())
    line.append((a,b))
line.sort()
l=[0]
for i in line:
    l.append(i[1])

d=[1 for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,i):
        if l[i]>l[j]:
            d[i]=max(d[i],d[j]+1)

print(n-max(d))
