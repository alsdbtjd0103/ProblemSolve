from collections import deque
import copy
import sys
input=sys.stdin.readline
def check(arr):
    visited=[[False]*m for i in range(n)]
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    ans=0
    for i in range(n):
        if ans>1:
            break
        for j in range(m):
            if ans>1:
                break
            if arr[i][j]!=0 and not visited[i][j]:
                ans+=1
                que=deque([(i,j)])
                visited[i][j]=True
                while que:
                    x,y=que.popleft()
                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k]
                        if nx>=0 and ny>=0 and nx<n and ny<m and not visited[nx][ny] and arr[nx][ny]!=0:
                            visited[nx][ny]=True
                            que.append((nx,ny))

    if ans>1:
        return True
    else:
        return False

def is_finished(arr):
    
    for i in range(n):
        for j in range(m):
            if arr[i][j]!=0:
                return False
    return True


n,m=map(int,input().split())
arr=[]

for i in range(n):
    arr.append(list(map(int,input().split())))

answer=0

while True:
    temp_arr=copy.deepcopy(arr)
    if is_finished(arr):
        answer=0
        break
    if check(arr):
        break
    answer+=1
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]

    for i in range(n):
        for j in range(m):
            if temp_arr[i][j]!=0:
                num=0
                for k in range(4):
                    nx,ny=i+dx[k],j+dy[k]
                    if nx>=0 and ny>=0 and nx<n and ny<m and temp_arr[nx][ny]==0:
                        num+=1
                arr[i][j]=max(arr[i][j]-num,0)
    temp_arr=copy.deepcopy(arr)

print(answer)
