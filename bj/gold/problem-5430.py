import copy

t=int(input())
result=[]
for i in range(t):
    p=input()
    n=int(input())
    arr=input()
    arr=arr.replace('[','')
    arr=arr.replace(']','')
    arr=arr.replace(',',' ')
    arr=list(map(int,arr.split()))
    arr2=copy.deepcopy(arr)
    num=p.count('D')
    standard=0
    loc=True
    error=0
    for j in range(num):
        if len(arr2)==0:    ##수정은 arr2에 적용하고 arr는 D를 찾는 용도
            result.append('error')
            error=1
            break
            
        temp=p.find('D',standard)

        if temp-standard==0:
            loc=loc
        elif j==0 and (temp-standard)%2==1:
            loc=not loc
        elif j==0 and (temp-standard)%2==0:
            loc=loc
        elif (temp-standard)%2==1:
            loc=not loc
    
            
        if loc:
            z=arr2.pop(0)
        else:
            z=arr2.pop(-1)
        standard=temp+1

    if p.count('R')%2==0 and error==0:
        result.append(arr2)
    elif error==0:
        arr2.reverse()
        result.append(arr2)
    
        
for k in result:    ##이 문제에서 입출력은 리스트 그대로 출력하면 안되고 띄어쓰                        기를 없애야한다.        
    if k=='error':
        print(k)
    else:
        x='['
        for z in k:
            x+=str(z)
            x+=','
        if ',' in x:    ##빈 리스트가 답일 경우를 대비
            x=x[:-1]
        x+=']'
        print(x)
            
        
            
        
        
        
        

