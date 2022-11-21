import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    a[i]=(i,a[i])

stack=[]
result=[0 for i in range(n)]
for i in a:
    if not stack:
        stack.append(i)
    else:
        while True and stack:
            index, value=stack.pop()
            if value<i[1]:
                result[index]=i[1]
            else:
                stack.append((index,value))
                break
        stack.append(i)
for index,val in stack:
    result[index]=-1
                
print(' '.join(map(str,result)))

