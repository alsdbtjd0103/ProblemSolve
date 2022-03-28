from heapq import *

def solution(food_times, k):
    answer=0
    minus_number=0
    if k>=sum(food_times):    # 다 먹어버림
        return -1
    
    hq=[]
    for i in range(len(food_times)):
        heappush(hq,(food_times[i],i))
    while hq:
        temp1=heappop(hq)
        temp=(temp1[0]-minus_number,temp1[1])
        if temp[0]<=0:
            continue
        if k>=(len(hq)+1)*temp[0]:
            minus_number+=temp[0]
            k-=(len(hq)+1)*temp[0]
        else:
            heappush(hq,(temp[0],temp[1]))
            hq.sort(key=lambda num:num[1])
            result=hq[k%len(hq)]
            answer=result[1]+1
            break
    return answer
    
                
            
        
        
        
    
    
    
food_times=[8,6,4]
k=1

print(solution(food_times,k))
