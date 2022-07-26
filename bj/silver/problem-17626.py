import math
n = int(input())
d = [0, 1]
for i in range(2, n+1):
    temp=1
    l=[]
    for j in range(1,int(math.sqrt(i))+1):
        if j*j>i:
            break
        l.append(d[i-j*j])
    d.append(min(l)+1)
        

print(d[n])
