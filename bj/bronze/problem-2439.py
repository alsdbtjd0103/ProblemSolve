n=int(input())

for i in range(0,n):
    arr=[' ' for _ in range(n)]
    for j in range(n-(i+1),n):
        arr[j]='*'
    print(''.join(arr))