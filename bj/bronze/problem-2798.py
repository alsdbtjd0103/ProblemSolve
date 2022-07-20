from itertools import combinations
n,m=map(int,input().split())
card = list(map(int,input().split()))
com=combinations(card,3)
result=m
for c in com:
    d=m-sum(c)
    if d>=0 and d<result:
        result=d
        
print(m-result)
