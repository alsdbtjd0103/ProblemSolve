n=int(input())
two=0
five=0

for i in range(n,1,-1):
    temp=i
    while True:
        if temp/2==int(temp/2):
            two+=1
            temp/=2
        elif temp/5==int(temp/5):
            five+=1
            temp/=5
        else:
            break

print(min(two,five))