from collections import defaultdict
import sys
input=sys.stdin.readline
dic=defaultdict(str)
result=[]
n,m=map(int,input().split())
for _ in range(n):
    a,b=input().rstrip().split()
    dic[a]=b
for _ in range(m):
    a=input().rstrip()
    result.append(dic[a])
for r in result:
    print(r)
