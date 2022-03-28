# 01이 마주하면 같이 돌아감
# 2번과 6번 톱니를 확인해야함
# 바로 돌리지말고 전체 다 확인하고 돌려야함
# 오래 걸린 이유
# 1. 언제 2번 6번 비교하고 6번 2번 비교해야하는지 헷갈림
# 2. temp_direction이 같이 바뀌는게 아니라 각 s,t관련 if문이 실행될때마다 따로 바뀌기 때문에 두개로 나눠서 성정해줘야함.

from collections import deque
num1=deque(list(map(int,input())))
num2=deque(list(map(int,input())))
num3=deque(list(map(int,input())))
num4=deque(list(map(int,input())))
wheel=[0,num1,num2,num3,num4,0]

k=int(input())
rotate=[]
for i in range(k):
    a,b=map(int,input().split())
    rotate.append((a,b))

def rotate_wheel(num,direction):
    if direction==1:
        temp=wheel[num].pop()
        wheel[num].appendleft(temp)
    else:
        temp=wheel[num].popleft()
        wheel[num].append(temp)

        

for i in range(len(rotate)):
    which_rotate=[]
    number,direction=rotate[i][0],rotate[i][1]
    which_rotate.append((number,direction))
    s,t=number-1,number+1
    if direction==1:
        temp_direction_s=-1
        temp_direction_t=-1
    else:
        temp_direction_s=1
        temp_direction_t=1
    while True:
        if s>0:
            if wheel[s][2]!=wheel[s+1][6]:
                which_rotate.append((s,temp_direction_s))
                temp_direction_s*=-1
            else:
                s=-1
                
        if t<5:
            if wheel[t][6]!=wheel[t-1][2]:
                which_rotate.append((t,temp_direction_t))
                temp_direction_t*=-1
            else:
                t=5
        if s<=0 and t>=5:
            break
        s-=1
        t+=1
    #print("which rotate: ",which_rotate)
    for w in which_rotate:
        rotate_wheel(w[0],w[1])
  #  for wh in wheel:
  #      if type(wh)!=int:
  #          print(wh)
    #print("--------------------")
score=0
for i in range(1,5):
    score+=wheel[i][0]*pow(2,i-1)
    #print(f"num {i}: {wheel[i][0]}")
    
print(score)
        
    
        
    

    

                
                    
        
    
    
    