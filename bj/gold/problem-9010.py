# 먼저 operation에서 내가 직접 list(map)어쩌구 이런식으로 하나하나 변한시키니까
# 시간초과가 나서 temp[:]를 이용함
# 그리고 이건 네자리수 기준이라는 것을 몰랐었음 (질문검색)
# 123은 사실 0123이라서 L을 실행하면 1230이나와야하고
# R을 실행하면 3012 가 나와야함.


from collections import deque

def operation(alpha,n):
    if alpha=='D':
        n=int((n*2)%10000)
    elif alpha=='S':
        if n==0:
            n=10000
        n=n-1

    elif alpha=='L':
        temp=str(n)
        if len(temp)<4:
            temp=('0'*(4-len(temp)))+temp
            
        n=int(temp[1:]+temp[0])

    elif alpha=='R':
        temp=str(n)
        if len(temp)<4:
            temp=('0'*(4-len(temp)))+temp
        n=int(temp[-1]+temp[0:-1])

    return n
    
        
def bfs(visited,v):
    start,destination=v
    que=deque([start])
    visited[start]=0
    while que:
        x=que.popleft()
        if x==destination:
            break
        for i in d:
            nx=operation(i,x)
            if visited[nx]==-1 and 0<=nx<10000:
                que.append(nx)
                visited[nx]=visited[x]+1
                distance[nx]=(x,i)
                if x==destination:
                    break
            
    
    
    
t=int(input())

d=['D','S','L','R']
result=[]
for i in range(t):
    a,b=map(int,input().split())
    visited=[-1]*10000
    distance=[0]*10000
    bfs(visited,(a,b))
    num=visited[b]
    r=[]
    for j in range(num):
        x,y=distance[b]
        r.append(y)
        b=x
    r.reverse()
    result.append("".join(r))
    
for i in result:
    print(i)
    

    
    

    
    
    
    
    