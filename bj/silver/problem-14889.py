from itertools import combinations
import copy
n=int(input())
s=[]
person = [i for i in range(n)]
for i in range(n):
    s.append(list(map(int,input().split())))

com = combinations(person,n//2)

min_n=1e9

for p in com:
    temp = copy.deepcopy(person)
    num=0
    for i in p:
        temp.remove(i)
        for j in p:
            num+=s[i][j]
    for i in temp:
        for j in temp:
            num-=s[i][j]
    if min_n>abs(num):
        min_n = abs(num)
    if min_n==0:
        break
print(min_n)

            
    
