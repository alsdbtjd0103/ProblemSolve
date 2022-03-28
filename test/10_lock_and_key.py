import copy
def rotation_90(arr,q):    # 시계 방향으로 90도 회전하는 함수
    temp=[[0]*q for i in range(q)]
    for i in range(q):
        for j in range(q):
            temp[j][q-1-i]=arr[i][j]
    return temp


def check(key,lock):
    num_key,num_lock=0,0
    for i in key:
        if i==1:
            num_key=num_key+1
        else:
            continue
    for k in lock:
        if k==1:
            num_lock=num_lock+1
        else:
            continue
    if num_key>num_lock:
        return False
    return True


def check_key(key,lock):
    result=1
    for i in range(2*n):
        for j in range(2*n):
            temp=copy.deepcopy(lock)
            for k in range(m):
                for z in range(m):
                    temp[i+k][j+z]+=key[k][z]

            for x in range(n,2*n):
                for y in range(n,2*n):
                    if temp[x][y]!=1:
                        result=0
            if result==1:
                print('temp: ')
                print(temp)
                return True
            else:
                result=1
                        
    return False
                        
            
                        
                
    
def solution(key,lock):
    answer=False
    if not check(key,lock):
        return answer
    temp=[[0]*(3*n) for _ in range(3*n)]
    for i in range(n,2*n):    # lock 3배 확장 후 가운데에 기존 lock 값 넣기
        for j in range(n,2*n):
            temp[i][j]=lock[i-n][j-n]
    extended_lock=temp
    for _ in range(4):
        result=check_key(key,extended_lock)
        print('key: ')
        print(key)
        if result:
            answer=True
            return answer
        key=rotation_90(key,m)
    return answer
    

key=[[1,1]]
lock=[[1,1],[1,1]]
m=len(key)
n=len(lock)

result=solution(key,lock)
print(result)

        
            
        
            


