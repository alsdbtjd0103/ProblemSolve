arr=[1,2,3,4,5,6,7,8]
a=list(map(int,input().split()))
if a==arr:
    print('ascending')
elif a==sorted(arr,reverse=True):
    print('descending')
else:
    print('mixed')