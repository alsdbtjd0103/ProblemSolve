from itertools import combinations

l,c=map(int,input().split())
alpha=list(input().split())
must=['a','e','i','o','u']

coms = combinations(alpha,l)
result=[]
for com in coms:
    a,b=0,0
    for c in com:
        if c in must:
            a+=1
        else:
            b+=1
    if a>=1 and b>=2:
        temp=list(com)
        temp.sort()
        result.append(temp)
result.sort()
for r in result:
    print(''.join(r))

