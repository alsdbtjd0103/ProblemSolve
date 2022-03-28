## 그냥 in을 써버리면 시간초과
## 여기서 sort를 하면 사전 숫자 순서대로 정렬됨
## 즉 a,b,c,d가 있고 만약 c가 a를 포함한다면 b도 무조건 a를 포함하게됨
## 따라서 i번쨰 요소랑 i+1번째 요소중 i.length 만큼만 확인하면 시간단축

import sys
input=sys.stdin.readline

t=int(input().rstrip())
result=[]
for _ in range(t):
    n=int(input().rstrip())
    loc=True
    arr=[]
    for i in range(n):
        arr.append(input().rstrip())
    
    
    arr.sort()

    for i in range(n-1):
        length=len(arr[i])
        if arr[i] == arr[i+1][:length]:
            result.append("NO")
            loc=False
            break
    if loc:
        result.append("YES")
        
        
for i in result:
    print(i)