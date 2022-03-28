# b를 a로 만드는 접근방법이 필요

a,b=map(int,input().split())
num=0
while True:
    if b<=a:
        if a==b:
            print(num+1)
        else:
            print(-1)
        break
    if b%2==0:
        b=b//2
        num+=1
    elif (b-1)%10==0:
        b=(b-1)//10
        num+=1
    else:
        b=-1



# 메모리초과이다. 아마 1e9만큼의 배열을 만드는게 어려운거같다.

# from collections import deque
# a,b=map(int,input().split())
# visited=[-1 for i in range(b+1)]
# def bfs(visited,start,destination):
#     que=deque([start])
#     visited[start]=0
#     while que:
#         x=que.popleft()
#         nx_1=x*2
#         nx_2=x*10+1
#         if nx_1<=destination and visited[nx_1]==-1:
#             visited[nx_1]=visited[x]+1
#             que.append(nx_1)
#         if nx_2<=destination and visited[nx_2]==-1:
#             visited[nx_2]=visited[x]+1
#             que.append(nx_2)
#         if nx_1==destination or nx_2==destination:
#             break
# bfs(visited,a,b)
# if visited[b]==-1:
#     print(-1)
# else:
#     print(visited[b]+1)

    