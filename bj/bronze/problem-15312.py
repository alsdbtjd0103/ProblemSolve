
import sys
sys.setrecursionlimit(1000000)
alpha=[ 3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
a=input()
b=input()
c=[]
for i in range(len(a)):
    c.append(alpha[ord(a[i])-65])
    c.append(alpha[ord(b[i])-65])
    
def func(arr):
    if len(arr)<=2:
        return (arr[0],arr[1])
    temp=[]

    for i in range(0,len(arr)-1):
        temp.append((arr[i]+arr[i+1])%10)
    return func(temp)

x,y=func(c)
print(x,end='')
print(y)
