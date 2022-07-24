import math
a,b,v=map(int,input().split())

dis=a-b

temp = math.ceil(v-b/dis)

print(temp)