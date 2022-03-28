p=[0]*(101)
p[1:11]=[1,1,1,2,2,3,4,5,7,9]
n=[]
t=int(input())
for i in range(t):
    n.append(int(input()))

for k in n:
    if k<=10:
        print(p[k])
    else:
        for x in range(11,k+1):
            p[x]=p[x-3]+p[x-2]
        print(p[k])
        

