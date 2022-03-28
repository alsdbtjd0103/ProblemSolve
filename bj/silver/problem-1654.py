#3 처음엔 잘 이해가 안됐는데 이제는 이해함
# 우선 반 잘라놓고 개수가 만들어지면 좀 더 적게 잘라도되는지 확인하는 과정

import sys
input=sys.stdin.readline
lan=[]
k,n=map(int,input().rstrip().split())
for i in range(k):
    lan.append(int(input()))
    
start=1
end=max(lan)
result=-1
while start<=end:
    mid=(start+end)//2
    count=0
    for i in lan:
        count+=i//mid
    if count>=n:
        result=mid
        start=mid+1
    else:
        end=mid-1
        
print(result)
        
