n=int(input())
data=[0]*301
score=[0]*301
for i in range(1,n+1):
    data[i]=int(input())
score[1]=data[1]
score[2]=data[1]+data[2]
score[3]=max(data[1]+data[3],data[2]+data[3])
for i in range(4,n+1):
    score[i]=max(score[i-3]+data[i-1]+data[i],score[i-2]+data[i])


print(score[n])

# 이 문제는 dp 문제로 두 가지 경우의 점화식을 세울 수 있다.
# 1. 마지막 계단을 밟고 그 전 계단을 밟을 경우
# - d[n]=d[n-3]+value[n-1]+value[n]
# 2. 마지막 계단을 밟고 그 전 계단을 밟지 않을 경우
# - d[n]=d[n-2]+value[n]

# 이 두 경우의 수 중 값이 더 큰 것을 선택하면 된다.

# 여기서 data를 append가 아니라 값을 대입하는 방법을 선택한 이유는
# 대입하는 방법을 쓰지 않으면 n=1 일때, 2일 때 3 일 때, 그 외의 경우에 대해
# 따로따로 만들어야한다. (list index out of bound)

    


