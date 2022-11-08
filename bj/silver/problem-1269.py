n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(len(set(a+b))-(len(a)+len(b)-len(set(a+b))))