s=int(input())

i=1
while True:
    temp = i*(i+1)//2
    if temp>s:
        break
    i+=1
print(i-1)