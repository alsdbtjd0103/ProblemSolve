## 풀긴했는데 그냥 stack에 temp에 in을 쓰면 시간초과남.. 다시풀자

## temp를 deque로 만들어면서 앞에껏만 pop하면서 하니까 시간 통과
## python3로도 통과
## 이거하나푸는데 너무 오래걸린다..

## 근데 풀이보니까 입력받을때부터 바로 비교해서 푼다..개고생했네
## 아 착각했던게 n=8이면 8개의 다른 수가 오는 줄 알았는데
## 그냥 1-8까지 오는구나..슈발

from collections import deque

import sys
input=sys.stdin.readline
n=int(input().rstrip())
arr=[]
for i in range(n):
    arr.append(int(input().rstrip()))
temp=deque(sorted(arr))
stack=[]
ans=[]
flag=True
loc=False
i=0
result=[]
while i<n:
    num=i
    i=i+1
    target=arr[num]
    if (not temp and stack) or loc:
        pop_num=stack.pop()
        result.append('-')
        loc=False
        if pop_num!=target:
            flag=False
            break
        else:
            ans.append(pop_num)
            continue

    for j in range(len(temp)):
        if target>temp[0]:
            stack.append(temp.popleft())
            result.append('+')
        elif target==temp[0]:
            stack.append(temp.popleft())
            result.append('+')
            ans.append(stack.pop())
            result.append('-')
            break
        elif target<temp[0]:
            loc=True
            i=i-1
            break

    if not flag:
        break

if len(ans)==n:
    for i in result:
        print(i)
        
else:
    print("NO")
    
        
            
            
            
                
                
                