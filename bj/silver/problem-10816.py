#아무리 이진탐색이라도 여러번 사용하는 알고리즘이라서 그런지 pypy3로해야만 통과
# 할 줄 알았는데 40퍼대에서 결국 시간초과..
#그냥 bisect 모듈 사용

import sys
import bisect
input=sys.stdin.readline
n=int(input().rstrip())
card=list(map(int,input().rstrip().split()))
m=int(input().rstrip())
number=list(map(int,input().rstrip().split()))
card.sort()
count=[0 for _ in range(m)]
num=-1
# def binary_search(start,end,target):
#     global num
#     if start>end:
#         return False
#     mid=(start+end)//2
#     if card[mid]>target:
#         return binary_search(start,mid-1,target)
#     elif card[mid]<target:
#         return binary_search(mid+1,end,target)
#     else:
#         num=mid
#         return True
#     return False

# for i in range(len(number)):
#     temp=binary_search(0,n-1,number[i])
#     temp_num=num
#     if temp:
#         s,d=0,0
#         while True:
#             t=binary_search(0,num-1,number[i])
#             if not t:
#                 s=num
#                 break
#         num=temp_num
#         while True:
#             t=binary_search(num+1,n-1,number[i])
#             if not t:
#                 d=num
#                 break
#         count[i]=d-s+1
#     else:
#         count[i]=0
for i in range(len(number)):
    count[i]=bisect.bisect_right(card,number[i])-bisect.bisect_left(card,number[i])
            
        
            
for i in count:
    print(i,end=" ")