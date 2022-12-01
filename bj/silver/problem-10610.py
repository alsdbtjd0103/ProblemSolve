n=int(input())
num=list(str(n))
num.sort(reverse=True)

if num[-1]!='0':
    print(-1)
else:
    temp=[int(i) for i in num]
    if sum(temp)%3==0:
        print(''.join(num))
    else:
        print(-1)

