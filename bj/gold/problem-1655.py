import sys
import heapq
input = sys.stdin.readline
n = int(input())
q1, q2 = [], []
result = []
for _ in range(n):
    num = int(input())
    if not q1:
        heapq.heappush(q1, -1*num)
        result.append(num)
        continue

    temp = -1*heapq.heappop(q1)  # 하나를 뺌
    if len(q1) == len(q2):  # q2에 넣어야함
        if not q2:  # q2가 없을때 q1에서 하나 뺀거랑 인풋이랑 비교해서 넣음
            heapq.heappush(q2, max(temp, num))
            heapq.heappush(q1, -1*min(temp, num))
        else:  # q2가 있을때 q2의 최솟값 temp2를 뽑아서 num이랑 비교
            temp2 = heapq.heappop(q2)
            if num >= temp2:  # num이 temp2보다 크면 무조건 q2로 바로들어감
                heapq.heappush(q2, temp2)
                heapq.heappush(q2, num)
                heapq.heappush(q1, -1*temp)
            else:  # num이 temp2보다 작으면 temp와 비교해서
                if temp <= num:  # temp보다 크거나 같으면 바로 q2로 집어넣음
                    heapq.heappush(q2, num)
                    heapq.heappush(q2, temp2)
                    heapq.heappush(q1, -1*temp)
                else:  # temp보다 작으면 num이 q1으로 들어가고 temp가 q2로 들어감
                    heapq.heappush(q1, -1*num)
                    heapq.heappush(q2, temp)
                    heapq.heappush(q2, temp2)
    else:  # q1에 넣어야함 ->적어도 q2에 하나는 있음
        temp2 = heapq.heappop(q2)
        if num > temp2:  # num이 q2의 최솟값보다 크면 q2의 최솟값을 q1에다 넣고 num을 q2에 넣음
            heapq.heappush(q2, num)
            heapq.heappush(q1, -1*temp2)
            heapq.heappush(q1, -1*temp)
        else:  # num이 q2의 최솟값보다 작으면 바로 q1에 집어넣음
            heapq.heappush(q2, temp2)
            heapq.heappush(q1, -1*num)
            heapq.heappush(q1, -1*temp)

    ans = heapq.heappop(q1)*-1
    heapq.heappush(q1, ans*-1)
    result.append(ans)

for r in result:
    print(r)