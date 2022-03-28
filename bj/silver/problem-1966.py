import sys
input=sys.stdin.readline
t=int(input())
results=[]
while t>0:
    t-=1
    n,m=map(int,input().rstrip().split())
    arr=list(map(int,input().rstrip().split()))
    for i in range(n):
        arr[i]=(arr[i],i)
    count=0
    while True:
        if arr[0]==max(arr, key=lambda x:(x[0])):
            count+=1
            if arr[0][1]==m:
                results.append(count)
                break
            else:
                arr.pop(0)
        else:
            arr.append(arr[0])
            arr.pop(0)






for i in results:
    print(i)
