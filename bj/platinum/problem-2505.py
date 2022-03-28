## 변화가 없어도 된다는 것을 깜빡
## 그리고 뒤에서도 한번 확인해야함
def rever(arr,start,end):
    arr[start:end+1]=reversed(arr[start:end+1])

    
import sys
input=sys.stdin.readline
n=int(input().rstrip())
arr=[0]
arr+=list(map(int,input().rstrip().split()))
arr2=arr[:]
ans_arr=[i for i in range(0,n+1)]
start=0
end=0
result=[]
for i in range(1,n+1):
   # print("i: ",i,"arr[i]: ",arr[i])
    if i!=arr[i]:
        start=i
        break
for i in range(start,n+1):
    if start!=0 and arr[i]==start:
        end=i
        break

#print("start: ",start,"end: ",end)
rever(arr,start,end)
if start==0 and end==0:
    start,end=1,1
result.append((start,end))
#print(arr)
start,end=0,0

for i in range(1,n+1):
    #print("i: ",i,"arr[i]: ",arr[i])
    if i!=arr[i]:
        start=i
        break
for i in range(start,n+1):
    if start!=0 and arr[i]==start:
        end=i
        break
#print("start: ",start,"end: ",end)
rever(arr,start,end)
if start==0 and end==0:
    start,end=1,1
result.append((start,end))

if arr==ans_arr:
    for x,y in result:
        print(x,y)
else:

    start=0
    end=0
    result=[]
    for i in range(n,0,-1):
       # print("i: ",i,"arr[i]: ",arr[i])
        if i!=arr2[i]:
            start=i
            break
    for i in range(start,0,-1):
        if start!=0 and arr2[i]==start:
            end=i
            break
    rever(arr2,end,start)
    if start==0 and end==0:
        start,end=1,1
    result.append((end,start))
    end,start=0,0
    
    for i in range(n,0,-1):
       # print("i: ",i,"arr[i]: ",arr[i])
        if i!=arr2[i]:
            start=i
            break
    for i in range(start,0,-1):
        if start!=0 and arr2[i]==start:
            end=i
            break
    rever(arr2,end,start)
    if start==0 and end==0:
        start,end=1,1
    result.append((end,start))
    for x,y in result:
        print(x,y)

        
    
