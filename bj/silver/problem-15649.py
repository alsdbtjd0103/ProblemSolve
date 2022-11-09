from itertools import permutations
n,m=map(int,input().split())
a=[i for i in range(1,n+1)]

p=permutations(a,m)
for per in p:
    for k in per:
        print(k,end=' ')
    print('')