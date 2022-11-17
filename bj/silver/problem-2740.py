a,b=[],[]
n,m=map(int,input().split())

for _ in range(n):
    a.append(list(map(int,input().split())))

m,k=map(int,input().split())

for _ in range(m):
    b.append(list(map(int,input().split())))

ans=[]

temp1=[]
for i in range(k):
    t=[]
    for j in range(m):
        t.append(b[j][i])
    temp1.append(t)

temp2=[]
for i in range(n):
    temp3=[]
    for temp in temp1:
        result=0
        for t in range(len(temp)):
            result+=a[i][t]*temp[t]
        temp3.append(result)
    temp2.append(temp3)
ans=temp2
        
for i in ans:
    for j in i:
        print(j,end=' ')
    print('')

    

    


