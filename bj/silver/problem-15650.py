from itertools import combinations
n,m=map(int,input().split())
a=[i for i in range(1,n+1)]
com=combinations(a,m)
for i in com:
    for j in i:
        print(j,end=' ')
    print('')
