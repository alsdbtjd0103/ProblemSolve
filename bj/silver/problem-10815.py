n=int(input())
card=list(map(int,input().split()))
m=int(input())
number=list(map(int,input().split()))
card.sort()

def binary_search(start,end,target):
    if start>end:
        return False
    mid=(start+end)//2
    # print("start: ",start,"end: ",end)
    # print("mid: ",card[mid],"target: ",target)
    
    if card[mid]>target:
        return binary_search(start,mid-1,target)
    elif card[mid]<target:
        return binary_search(mid+1,end,target)
    elif card[mid]==target:
        
        return True
    return False

result=[]
for i in number:
    temp=binary_search(0,n-1,i)
    if temp:
        result.append(1)
    else:
        result.append(0)
        
for i in result:
    print(i,end=' ')
    

