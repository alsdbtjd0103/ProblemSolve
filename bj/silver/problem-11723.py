import sys
m=int(input())
s=[]
for i in range(m):
    temp=sys.stdin.readline().rstrip()
    if ' ' in temp:
        oper,x=temp.split()
        x=int(x)
    else:
        oper=temp
    if oper=='add':
        if x not in s:
            s.append(x)
    if oper=='remove':
        if x in s:
            s.remove(x)
    if oper=='check':
        if x in s:
            print(1)
        else:
            print(0)
    if oper=='toggle':
        if x in s:
            s.remove(x)
        else:
            s.append(x)
    if oper=='all':
        s=[j for j in range(1,21)]
    if oper=='empty':
        s=[]