import sys
input = sys.stdin.readline
n, m = map(int, input().split())

num = list(map(int, input().split()))
result = []
num_sum=0
s=[]
for i in range(len(num)):
    num_sum+=num[i]
    s.append(num_sum)

for _ in range(m):
    i, j = map(int, input().split())
    i,j=i-1,j-1
    ans=s[j]-s[i]+num[i]
    result.append(ans)


for r in result:
    print(r)



# 누적합 이용..
# 첫번째부터j번째까지의 합 - 첫번째부터 i번쨔까지의 합 + i번째 수 

