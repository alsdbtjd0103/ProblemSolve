from itertools import combinations
n,s=map(int,input().split())
a=list(map(int,input().split()))
count=0
for i in range(1,n+1):
    c=list(combinations(a,i))
    for j in c:
        if sum(j)==s:
            count+=1
print(count)
            