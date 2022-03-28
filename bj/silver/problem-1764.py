import sys
input=sys.stdin.readline
n,m=map(int,input().rstrip().split())

listen=set([])
watch=set([])
for i in range(n+m):
    if i<n:
        listen.add(input().rstrip())
    else:
        watch.add(input().rstrip())
both=list(listen & watch)
print(len(both))
both.sort()
for i in both:
    print(i)