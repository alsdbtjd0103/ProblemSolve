n,m=map(int,input().split())
result1=n
result2=m
if m>(n//2):
    m=n-m
    result2=m

for i in range(1,m):
    result1=result1*(n-i)

    result2=result2*(m-i)

print(result1//result2)
    