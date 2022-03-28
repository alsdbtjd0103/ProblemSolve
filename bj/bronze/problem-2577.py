a=int(input())
b=int(input())
c=int(input())
num=a*b*c
count=[0]*10
arr=(list(map(int,str(num))))
print(arr)
for i in arr:
    count[i]+=1
for i in count:
    print(i)
    