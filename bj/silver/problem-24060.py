
def merge_sort(temp,p,r):
    if p<r:
        q=(p+r)//2
        merge_sort(temp,p,q)
        merge_sort(temp,q+1,r)
        merge(p,q,r)

def merge(p,q,r):
    global ans,cnt
    tmp=[]
    i,j,t=p,q+1,0
    while i<=q and j<=r:
        if temp[i]<=temp[j]:
            tmp.append(temp[i])
            i+=1
        else:
            tmp.append(temp[j])
            j+=1
    while i<=q:
        tmp.append(temp[i])
        i+=1
    while j<=r:
        tmp.append(temp[j])
        j+=1
    i=p
    for z in range(i,r+1):
        temp[z]=tmp[t]
        if cnt==k:
            ans=temp[z]
        t+=1
        cnt+=1
    
n,k=map(int,input().split())
temp=list(map(int,input().split()))

global ans,cnt
cnt,ans=1,-1

merge_sort(temp,0,n-1)
print(ans)
