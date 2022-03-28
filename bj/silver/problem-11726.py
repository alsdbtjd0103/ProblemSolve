n=int(input())
d=[0]*1002
d[1]=1
d[2]=2
if n>2:
    for i in range(3,n+1):
        d[i]=(d[i-1]+d[i-2])%10007

print(d[n])
    
# 이 문제는 dp 문제로 처음 시작은 2x1 타일 하나거나 1x2 타일 두 개가 올 경우밖에
# 존재하지 않는다
# 따라서 2x1 타일부터 시작하는 경우, d[i-1]의 개수만큼 존재하고
# 1x2 타일 두개로 시작하는 경우, d[i-2]의 개수만큼 존재하기 때문에
# 이 둘을 더하면 된다