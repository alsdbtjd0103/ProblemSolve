n=int(input())
arr=[]
arr=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())
minvalue=1e9
maxvalue=-1e9
i=1
def dfs(i,now):
    global add,sub,mul,div,maxvalue,minvalue
    if i==n:
        minvalue=min(minvalue,now)
        maxvalue=max(maxvalue,now)
    else:
        if add>0:
            add-=1
            dfs(i+1,now+arr[i])
            add+=1
        if sub>0:
            sub-=1
            dfs(i+1,now-arr[i])
            sub+=1
        if mul>0:
            mul-=1
            dfs(i+1,now*arr[i])
            mul+=1
        if div>0:
            div-=1
            dfs(i+1,int(now/arr[i]))
            div+=1
dfs(i,arr[0])
print(maxvalue)
print(minvalue)

    