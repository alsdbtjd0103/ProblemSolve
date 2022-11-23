import sys
input=sys.stdin.readline
n=int(input())
a=[int(input()) for _ in range(n)]
stack=[]

def func():
    ans=0
    for i in range(n):
        if not stack:
            stack.append((i,a[i]))
            
        else:
            if a[i]>=stack[-1][1]:
                stack.append((i,a[i]))
            else:
                z=i
                while stack:
                    if stack[-1][1]<=a[i]:
                        break
                    index,temp=stack.pop()
                    ans=max(ans,(i-index)*temp)
                    z-=1
    
                stack.append((z,a[i]))

    while stack:
        index,temp=stack.pop()
        ans=max(ans,temp*(i-index+1))
    return ans

result=func()
a.reverse()
result2=func()

print(max(result,result2))