import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
que=deque([])
while True:
    num=int(input())
    if num>0:
        if len(que)<n:
            que.append(num)
    if num==0:
        if que:
            que.popleft()
    if num==-1:
        if que:
            while que:
                print(que.popleft(),end=' ')
        else:   
            print('empty')
        break
