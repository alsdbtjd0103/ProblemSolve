n,x=map(int,input().split())
arr=list(map(int,input().split()))

def binary_search(start,end,target):
    if start>end:
        return False
    mid=(start+end)//2
    if arr[mid]>target:
        binary_search(start,mid-1,target)
    elif arr[mid]<target:
        binary_search(mid+1,end,target)
    else:
        return mid
    return False
count=-1
temp=binary_search(0,n-1,x)
a=temp
if temp:
    count=1
    while True:
        temp-=1
        if arr[temp]!=x:
                break
        else:
            count+=1

    temp=a
    while True:
        temp+=1
        if arr[temp]!=x:
            break
        else:
            count+=1

print(count)
        
        
    
    
            