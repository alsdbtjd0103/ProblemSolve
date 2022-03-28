from collections import deque

n,k=map(int,input().split())

result=[]
q=deque([i for i in range(1,n+1)])
while len(result)<n:
    for i in range(k-1):
        temp=q.popleft()
        q.append(temp)
        
    result.append(q.popleft())
print('<',end='')  
for i in range(len(result)):
    if i==len(result)-1:
        print(str(result[i])+'>')
    else:
        print(str(result[i])+', ',end='')
    