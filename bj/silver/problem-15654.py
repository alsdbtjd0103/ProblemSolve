from itertools import permutations
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
com=permutations(a,m)
for i in com:
    for j in i:
        print(j,end=' ')
    print('')
