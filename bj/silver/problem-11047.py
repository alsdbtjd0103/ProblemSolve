n,k=map(int,input().split())
a=[]
count=0
for i in range(n):
    a.append(int(input()))

for i in range(n-1,-1,-1):
    while k>=a[i]:
        value=k//a[i]
        k=k-value*a[i]
        count+=value
print(count)
    
# 그냥 그리디 알고리즘으로 가장 큰 단위부터 최대한 빼면 된다
# 그런데 그냥 빼면 시간초과 발생
# 따라서 그냥 빼지 말고 나눠서 최대한 게산 빠르게하자
