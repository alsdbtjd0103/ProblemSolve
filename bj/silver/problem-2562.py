arr=[]
maxnum=-1
for i in range(9):
    arr.append(int(input()))
print(max(arr))
for i in range(9):
    if arr[i]==max(arr):
        maxnum=i+1
print(maxnum)
        