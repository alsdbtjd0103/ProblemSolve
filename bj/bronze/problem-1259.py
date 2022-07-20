result=[]
while True:
    a=input()
    if a=='0':
        break
    if a==a[::-1]:
        result.append('yes')
    else:
        result.append('no')

for i in result:
    print(i)
    
