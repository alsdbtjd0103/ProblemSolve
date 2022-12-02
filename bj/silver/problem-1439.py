s=input()
a=''
for i in s:
    if not a:
        a+=i
        continue
    if i!=a[-1]:
        a+=i
num=[0,0]
for i in a:
    if i=='0':
        num[0]+=1
    else:
        num[1]+=1
print(min(num))
