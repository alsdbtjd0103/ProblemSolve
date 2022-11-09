n,m=map(int,input().split())
a=[]

def dfs():
    if len(a)==m:
        print(' '.join(map(str,a)))
        return
    for i in range(1,n+1):
        if i in a:
            continue
        a.append(i)
        dfs()
        a.pop()

dfs()


# from itertools import permutations
# n,m=map(int,input().split())
# a=[i for i in range(1,n+1)]

# p=permutations(a,m)
# for per in p:
#     for k in per:
#         print(k,end=' ')
#     print('')