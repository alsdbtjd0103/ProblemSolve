import sys
input=sys.stdin.readline
a=list()
num=-1




N=int(input())
for i in range(0,N):
  arr=input().split()
  if arr[0]=='push':
    temp=int(arr[1])
    num=num+1
    a.insert(num,temp)
  else:
    if arr[0]=='top':
        if num==-1:
          print(-1)
        else:
          print(a[num])
    elif arr[0]=='size':
        print(num+1)
    elif arr[0]=='empty':
      if num==-1:
        print(1)
      else:
        print(0)
    elif arr[0]=='pop':
      if num==-1:
        print(num)
      else: 
        print(a[num])
        num-=1
    else:
      print ("wrong input")
      break









