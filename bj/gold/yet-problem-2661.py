def check(num,i):
    for k in range((i+1)//2):
        if num[-1-k:]==num[2*(-1-k):-1-k]:
            return False
    return True

def make(num,i):
    global change
    change=True
    for j in range(1,4):
        if j in obstacle:
            continue
        for k in range((i+1)//2):
            if not check(i):
                num=num[:-1]
                change=False
                break
            change=True
            if len(num)==i+1:
                break
    return num

n=int(input())
num=""
change=True
obstacle=[]
for i in range(n):
    num=make(num,i)
    if check(num,i) and change:
        make(num+str)
        
    
              
    
print(num)