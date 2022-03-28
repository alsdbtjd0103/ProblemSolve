n=int(input())
p=list(map(int,input().split()))
p.sort()
result=0
for i in range(n,0,-1):
    result+=p[n-i]*i

print(result)

# 처음에는 dp문제라고 생각했으나 아님
# 이 문제는 각 사람마다 기다리는 시간을 모두 더하는 문제
# 먼저 나오는 숫자는 그만큼 더 반복되게 더해지는 구조이기 때문에
# 앞에 작은 숫자가 있을 수록 총 대기시간은 낮아짐
# (앞에 큰 숫자가 있으면 큰 숫자가 많이 반복되어 더해지기 때문)