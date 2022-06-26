
from collections import defaultdict
import sys
input=sys.stdin.readline
n,m=map(int,input().rstrip().split())
p=[]
dic=defaultdict()
dic2=defaultdict()
for i in range(n):
    temp=input().rstrip()
    dic[temp]=i+1
    dic2[i+1] = temp

for _ in range(m):
    q=input().rstrip()
    if ord(q[0])<65:
        print(dic2[int(q)])
    else:
        print(dic[q])


