a=input()
oper=['+','-']
num_list=[]
o_list=[]
index=0
for i in range(len(a)):
    if a[i]=='+' or a[i]=='-':
        num_list.append(int(a[index:i]))
        o_list.append(a[i])
        index=i+1

num_list.append(int(a[index:]))
index=1
num_sum=num_list[0]
for i in range(len(a)):
    if a[i] in oper:
        if a[i]=='+':
            num_sum+=num_list[index]
            index+=1

        if a[i]=='-':
            num_sum-=sum(num_list[index:])
            break
print(num_sum)
