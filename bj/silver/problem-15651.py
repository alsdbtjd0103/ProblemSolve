n,m=map(int,input().split())
a=[]
def dfs():
    if len(a)==m:
        print(' '.join(map(str,a)))
        return
    for i in range(1,n+1):
        a.append(i)
        dfs()
        a.pop()

dfs()