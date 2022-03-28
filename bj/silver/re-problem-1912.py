
n=int(input())
data=list(map(int,input().split()))
result=[data[0]]
for i in range(n-1):
    result.append(max(result[i]+data[i+1],data[i+1]))
print(max(result))

# 결국 검색을 통해서 풀이
# 기존에 계속 더하던 값 + 현재 값 vs 현재값 비교해서 최댓값 매번 갱신하는 방법
# 무조건 연속해야하기 때문에 기존에 연속된 값에다가 지금 값을 더하는게 그냥 지금 
# 값보다 더 작으면 그냥 지금 값을 선택하는게 베스트





# n=int(input())
# data=list(map(int,input().split()))
# max_n=-99999
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         value=sum(data[i-1:j])
#         if max_n<value:
#             max_n=value
# print(max_n)

# 이 코드는 메모리는 살렸지만 결국 시간이 부족해서 근본적인 원인이 해결되지 않았다.


# --------------------------------------------------------------

# # n=int(input())
# # data=list(map(int,input().split()))
# # d=[[0]*(n+1) for _ in range(n+1)]
# # max_n=-99999
# # for i in range(1,n+1):
# #     for j in range(i,n+1):
# #         d[i][j]=sum(data[i-1:j])
        
# #         if max_n<d[i][j]:
# #             max_n=d[i][j]

# # print(max_n)

# 위 방법은 답은 나오지만 메모리가 초과된다. 1<=n<=1000000 이기 때문에
# 배열의 크기가 말도안되게 커지기 때문

